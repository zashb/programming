import numpy as np
import pandas as pd

from scipy import stats
from sklearn import preprocessing
from sklearn import cluster
from sklearn import model_selection
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

from plotly.offline import plot
from plotly.graph_objs import *
from plotly import tools


class Solution:
    def __init__(self):
        self.seed = 5
        self.df = pd.DataFrame()
        self.df_validated = pd.DataFrame()
        self.cityDF_gby_std = pd.DataFrame()
        self.colList = []

    def main(self):
        self.df = self.loadData("sample.txt")
        self.df_validated = self.validateDF(self.df)

    def loadData(self, filename):
        filedir = r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\mktbaskanlys\\"
        df = pd.read_csv(filedir + filename)
        return df

    def describeData(self, df):
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)
        print("DTYPE COUNTS : \n", df.get_dtype_counts())
        print("DTYPES : \n", df.dtypes)
        for i in df.columns:
            print("NUM OF UNIQUES IN {0} : \n{1}".format(i, df[i].nunique(dropna=False)))

    def exploreDF(self, df):
        # diff ways of seeing correlations
        # 1 crosstab of y with some suspicious var
        print(pd.crosstab(df["is_booking"], df["srch_rm_cnt"]))
        # 2 how did a suspicious var vary with y
        print(df.groupby('srch_rm_cnt')["is_booking"].mean())
        # 3 checking corr of another var with y - this checks only lin corr
        print(df["srch_children_cnt"].corr(df["is_booking"]))
        # plot hists of cols similar to value_counts()
        histCols = ['channel', 'is_booking', 'is_mobile', 'orig_destination_distance', 'srch_rm_cnt', 'srch_adults_cnt',
                    'srch_children_cnt']
        fig = tools.make_subplots(rows=len(histCols), cols=1)
        x = 1
        for i in histCols:
            trace = Histogram(x=df[i], name=i)
            fig.append_trace(trace, x, 1)
            x += 1
        plot(fig,
             filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\mktBktAnlys\hist.html")
        # # booking rate distribution across users
        userBookingRate = df.groupby('user_id')["is_booking"].agg(["mean"]).reset_index()
        # method 1
        # bookingRateUserCount = userBookingRate.groupby("mean")["user_id"].agg(["count"]).reset_index()
        # method 2
        # bookingRateUserCount = userBookingRate["mean"].value_counts(dropna=False).reset_index()
        # trace = Bar(x=bookingRateUserCount["mean"], y=bookingRateUserCount["index"], orientation='h')
        # plot([trace],
        #      filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\mktBktAnlys\bookingDist.html")
        # method 3
        trace = Histogram(x=userBookingRate["mean"])
        layout = Layout(title='BOOKING RATE DISTRIBUTION ACROSS USERS', xaxis=dict(title='booking rate'),
                        yaxis=dict(title='# of users'))
        fig = Figure(data=[trace], layout=layout)
        plot(fig,
             filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\mktBktAnlys\bookingDist.html")

    def validateDF(self, df):
        # num of guests need to be > 0
        print(pd.crosstab(df["srch_adults_cnt"], df["srch_children_cnt"]))
        # while dropping rows, select the condition and then use.index
        df.drop(df[df["srch_adults_cnt"] + df["srch_children_cnt"] == 0].index, inplace=True)
        print(pd.crosstab(df["srch_adults_cnt"], df["srch_children_cnt"]))
        # conv cols to dt
        df['srch_co'] = pd.to_datetime(df['srch_co'])
        df['srch_ci'] = pd.to_datetime(df['srch_ci'])
        df['date_time'] = pd.to_datetime(df['date_time'])
        # extracting date from dt
        df['date'] = pd.to_datetime(df['date_time'].apply(lambda x: x.date()))
        # co date must be > ci date; ci date must be > booking date
        print("CO DATE < CI DATE : \n", df.loc[df["srch_co"] < df["srch_ci"], ["srch_co", "srch_ci"]])
        print("CI DATE < BOOKING DATE : \n", df.loc[df["srch_ci"] < df["date"], ["srch_ci", "date"]])
        # np.nan incorrect data
        df["duration"] = (df["srch_co"] - df["srch_ci"]).dt.days
        df["duration"] = df["duration"].apply(lambda x: np.nan if x < 0 else x)
        df["days_in_advance"] = (df["srch_ci"] - df["date"]).dt.days
        df["days_in_advance"] = df["days_in_advance"].apply(lambda x: np.nan if x < 0 else x)
        return df

    def getOutPerformingAndUnderPerformingChannels(self):
        # get booking rate for each channel
        print("BOOKING RATE FOR EACH CHANNEL : \n", self.df_validated.groupby("channel")["is_booking"].agg(
            {"booking_rate": "mean", "num_of_bookings": "count"}).reset_index().sort_values(by="booking_rate"))
        # get mean booking rate across df
        print("MEAN BOOKING RATE : \n", self.df_validated["is_booking"].mean())
        # test significance
        self.tComparison("channel")
        # from the above output we can say with confidence which segments are overperforming and which segments are underperforming

    # rem this whole damn thing
    def tComparison(self, col):
        # cal booking rate and count for the col
        cat = self.df_validated.groupby(col)["is_booking"].agg(
            {"sub_avg": "mean", "sub_bookings": "count"}).reset_index()
        # cal booking rate and count for the df
        cat["overall_avg"] = self.df_validated["is_booking"].mean()
        cat["overall_bookings"] = self.df_validated["is_booking"].count()
        # cal diff in count
        cat["rest_bookings"] = cat["overall_bookings"] - cat["sub_bookings"]
        # cal diff in rates
        cat["rest_avg"] = ((cat["overall_avg"] * cat["overall_bookings"]) - (cat["sub_avg"] * cat["sub_bookings"])) / \
                          cat["rest_bookings"]
        # Z = (p1-p2)/np.sqrt(p(1-p)(1/n1+1/n2))
        cat["z_score"] = (cat["sub_avg"] - cat["rest_avg"]) / \
        np.sqrt(cat["overall_avg"] * (1 - cat["overall_avg"]) * (1 / cat["sub_bookings"] + 1 / cat["rest_bookings"]))
        cat["prob"] = np.around(stats.norm.cdf(cat["z_score"]), decimals=10)
        cat["significant"] = [(lambda x: 1 if x > 0.9 else -1 if x < 0.1 else 0)(i) for i in cat["prob"]]
        print(cat)

    def clusterCities(self):
        # 1 select feats and build df; dont include city col here
        self.colList = ['duration', 'days_in_advance', 'orig_destination_distance', 'is_mobile', 'is_package',
                        'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt']
        cityDF = self.df_validated.dropna(axis=0)[self.colList + ["user_location_city"]]
        cityDF_gby = cityDF.groupby("user_location_city").mean().reset_index().dropna(axis=0)
        # 2 standardize data
        self.cityDF_gby_std = cityDF_gby.copy()
        for i in self.colList:
            self.cityDF_gby_std[i] = preprocessing.scale(self.cityDF_gby_std[i])
        # 3 select cluster method
        km = cluster.KMeans(n_jobs=-1, n_clusters=3, random_state=self.seed)
        self.cityDF_gby_std["cluster"] = km.fit_predict(self.cityDF_gby_std[self.colList])
        # 4 profile clusters by merging with city df
        print(pd.merge(cityDF_gby, self.cityDF_gby_std[["cluster", "user_location_city"]]).groupby("cluster").mean())

    def investigateHigherBookings(self):
        # merge cluster df with original df
        self.df_validated = self.df_validated.merge(self.cityDF_gby_std[['user_location_city', 'cluster']],
                                                    left_on='user_location_city', right_on='user_location_city',
                                                    how='outer')
        print(self.df_validated.groupby('cluster')['is_booking'].count())
        # build dtree
        tree_data = self.df_validated.dropna(axis=0)[self.df_validated['cluster'] == 2]
        tree_train, tree_test = model_selection.train_test_split(tree_data, test_size=0.2, random_state=self.seed,
                                                                 stratify=tree_data["is_booking"])
        clf = tree.DecisionTreeClassifier(max_leaf_nodes=6, min_samples_leaf=200)
        clf = clf.fit(X=tree_train[self.colList], y=tree_train["is_booking"])
        # viz dtree
        dot_data = StringIO()
        tree.export_graphviz(clf, out_file=dot_data,
                             feature_names=['duration', 'days_in_advance', 'orig_destination_distance', 'is_mobile',
                                            'is_package', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt'],
                             filled=True, rounded=True)
        pydot.graph_from_dot_data(dot_data.getvalue()).write_pdf(
            r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\mktBktAnlys\booking_tree.pdf")


if __name__ == "__main__":
    sol = Solution()
    sol.main()
    # sol.describeData(sol.df)
    # sol.exploreDF(sol.df)
    sol.getOutPerformingAndUnderPerformingChannels()
    # sol.clusterCities()
    # sol.investigateHigherBookings()
