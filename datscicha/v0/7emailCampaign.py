import numpy as np
import pandas as pd

from plotly.graph_objs import *
import cufflinks as cf
from plotly.offline import plot

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class Solution(object):
    # all methods in the analysis in sequence
    # def analyze(self):
    def __init__(self):
        # load data
        self.emailData = self.loadData("email_table.csv")
        self.openedData = self.loadData("email_opened_table.csv")
        self.clickedData = self.loadData("link_clicked_table.csv")
        # prelim clean
        for i in [self.emailData, self.openedData, self.clickedData]:
            i = self.prelimCleanDF(i)
        # merge
        self.df = self.mergeDF(self.emailData, self.openedData, self.clickedData)
        # viz insights
        # self.gbyDFList = self.get_vizInsights(self.df, ["email_text", "email_version", "hour", "weekday", "user_country", "user_past_purchases"])
        # set seed
        self.seed = 5
        # ml data prep
        self.df_ml = self.mlDataPrep(self.df)
        # feat imp df
        self.featImpDF = self.get_featImp(self.df_ml)
        # clus feat
        self.df_ml["clusLab"] = self.get_KNNClusters(self.df_ml)
        # feat imp df after clustering
        self.featImpDF = self.get_featImp(self.df_ml)

    # print basic DF description
    def getDF(self, df):
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)
        print("DTYPE COUNT : \n", df.get_dtype_counts())
        print("DTYPES : \n", df.dtypes)

    # load data and any necessary ETL
    def loadData(self, filename):
        filedir = r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\emailCampaign\\"
        df = pd.read_csv(filedir + filename)
        return df

    # preliminary clean
    def prelimCleanDF(self, df):
        for i in df.columns:
            # clean colnames
            i = i.strip()
            # strip obj cols
            if df[i].dtype == "object":
                df[i] = df[i].str.strip()
        return df

    # merge
    def mergeDF(self, ed, od, cd):
        # opened and clicked flag
        od["opened"] = 1
        cd["clicked"] = 1
        a = pd.merge(ed, od, on=["email_id"], how="left")
        df = pd.merge(a, cd, on=["email_id"], how="left")
        # fill 0 for not opened or clicked
        df["opened"] = df["opened"].fillna(0)
        df["clicked"] = df["clicked"].fillna(0)
        return df

    # verify
    def verify(self, df):
        clickedNotOpened = df.loc[(df["clicked"] == 1) & (df["opened"] != 1), "email_id"].tolist()
        print("# EMAIL IDs CLICKED WITHOUT OPENING: \n", len(clickedNotOpened))
        print("EMAIL IDs CLICKED WITHOUT OPENING: \n", clickedNotOpened)

    # pc opened, pc clicked
    def q1(self, df):
        df["opened"] = df["opened"].astype(int)
        df["clicked"] = df["clicked"].astype(int)
        opened_mean = df["opened"].mean()
        clicked_mean = df["clicked"].mean()
        print("% EMAIL IDs OPENED : \n", opened_mean)
        print("% EMAIL IDs CLICKED : \n", clicked_mean)

    # viz insights
    def get_vizInsights(self, df, colList):
        gbyDFList = []
        for col in colList:
            gby = df.groupby([col], as_index=False).agg({"clicked": np.mean})
            gby.columns = [col, "clicked"]
            gbyDFList.append(gby)
            trace = Bar(x=gby["clicked"], y=gby[col], orientation="h")
            layout = Layout(title="clicked_pc vs " + col,
                            xaxis=dict(title="clicked_pc"), yaxis=dict(title=col))
            fig = Figure(data=[trace], layout=layout)
            plot(fig,
                 filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\emailCampaignPlots\\" + col + ".html")
        return gbyDFList

    # data prep for ML
    def mlDataPrep(self, df):
        # deep copy to local df
        df_ml = df.copy()
        # dummify obj cols
        objCols = df_ml.select_dtypes(include=["object"]).columns
        df_ml = pd.get_dummies(df_ml, columns=objCols)
        # stringify email id col
        df_ml["email_id"] = df_ml["email_id"].astype(str)
        # conv all cols except emailid, past purchases to category
        for i in df_ml.columns:
            if i not in ["email_id", "user_past_purchases"]:
                df_ml[i] = df_ml[i].astype("category")
        return df_ml

    def get_featImp(self, df_ml):
        # get X,y; excluding for 2nd run
        Xcols = [i for i in df_ml.columns if i != "clicked" and i != "email_id"]
        X = df_ml.loc[:, Xcols]
        y = df_ml.loc[:, "clicked"]
        # get 10 fold cv mean
        self.get_10CVMean(X, y, RandomForestClassifier())
        # fit
        rf = RandomForestClassifier()
        rf.fit(X, y)
        # get feat imp
        featImpRel = 100 * rf.feature_importances_ / rf.feature_importances_.max()
        featImpDF = pd.DataFrame({"feat": list(Xcols), "featImpRel": list(featImpRel)})
        # plot
        trace = Bar(x=featImpDF["featImpRel"], y=featImpDF["feat"], orientation="h")
        plot([trace],
             filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\emailCampaignPlots\\" + "featImp.html")
        return featImpDF

    def get_10CVMean(self, X, y, estimator):
        estimator = estimator
        seed = self.seed
        kfold = StratifiedKFold(n_splits=10, random_state=seed)
        scoring = "accuracy"
        cv_res = cross_val_score(estimator, X, y, scoring=scoring, cv=kfold, n_jobs=-1)
        print("10 FOLD CV MEAN : \n", cv_res.mean())

    def get_KNNClusters(self, df_ml):
        df_ml_clus = df_ml.copy()
        km = KMeans(n_clusters=5, n_jobs=-1)
        df_ml_clus_scl = StandardScaler().fit_transform(df_ml_clus)
        km.fit_transform(df_ml_clus_scl)
        clusLab = list(km.labels_)
        return clusLab


if __name__ == "__main__":
    s = Solution()
    # s.getDF(s.emailData)
    # s.getDF(s.df)
    # s.verify(s.df)
    # s.q1(s.df)
    # for i in s.gbyDFList:
    #     print(i)
    s.getDF(s.df_ml)
    # s.getDF(s.featImpDF)
    # a = s.df_ml
    # a.to_pickle("temp_pkl.pkl")
