# source  - https://www.codementor.io/jadianes/data-science-python-pandas-r-dimensionality-reduction-du1081aka

import pandas as pd
from sklearn.decomposition import PCA
from plotly.graph_objs import *
import cufflinks as cf
from plotly.offline import plot
from sklearn.cluster import KMeans


class Solution:
    def __init__(self):
        self.seed = 5
        self.df = pd.DataFrame()
        self.df_pca = pd.DataFrame()

    def main(self):
        self.df = self.loadData("tb_existing_100.csv")
        self.df_pca = self.applyPCA(self.df)
        self.df_pca = self.getCountryMean(self.df)
        self.df_pca["cluster"] = self.getClusterLabels(self.df)
        self.df["cluster"] = self.getClusterLabels(self.df)

    def loadData(self, fileName):
        fileDir = r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\pca_kmeans_eda\\"
        df = pd.read_csv(fileDir + fileName, index_col=0, thousands=",")
        # setting colnames for  and cols
        df.index.names = ["country"]
        df.columns.names = ["year"]
        return df

    def describeDF(self, df):
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)
        print("DTYPE COUNTS : \n", df.get_dtype_counts())
        print("DTYPES : \n", df.dtypes)

    def applyPCA(self, df):
        pca = PCA(n_components=2)
        pca_tfrm = pca.fit_transform(df)
        pca_df = pd.DataFrame(pca_tfrm)
        # keep row index same as raw df
        pca_df.index = df.index
        pca_df.columns = ["PC1", "PC2"]
        print("EXPLAINED VARIANCE RATIO : \n", pca.explained_variance_ratio_)
        return pca_df

    def plotPC(self, df):
        # trace = Scatter(x=df["PC2"],y=df["PC1"],mode="markers",text = df.index,marker=dict(size=df["country_mean_scaled"]*100))
        trace = Scatter(x=df["PC2"], y=df["PC1"], mode="markers", text=df.index,
                        marker=dict(color=df['cluster'], showscale=True))
        plot([trace],
             filename=r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\plots\pca_kmeans\pca.html")

    def getCountryMean(self, df):
        # for each country get mean
        self.df_pca["country_mean"] = pd.Series(df.mean(axis=1))
        cntryMean_min = self.df_pca["country_mean"].min()
        cntryMean_max = self.df_pca["country_mean"].max()
        self.df_pca["country_mean_scaled"] = pd.Series((self.df_pca["country_mean"] - cntryMean_min) / cntryMean_max)
        return self.df_pca

    def getClusterLabels(self, df):
        kmeans = KMeans(n_jobs=-1, n_clusters=5, random_state=self.seed)
        clusters = kmeans.fit(df)
        return pd.Series(clusters.labels_, index=self.df_pca.index)

    def describeCluster(self, df):
        print(df["cluster"].value_counts())
        print(df.loc[df["cluster"] == 2, :])


if __name__ == "__main__":
    s = Solution()
    s.main()
    # s.describeDF(s.df_pca)
    # s.plotPC(s.df_pca)
    s.describeCluster(s.df)
