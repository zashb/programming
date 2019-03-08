import pandas as pd
from plotly.graph_objs import *


class Solution:
    def __init__(self):
        self.df = pd.DataFrame()
        self.corrDF = pd.DataFrame()

    def loadData(self):
        itemsDF = pd.read_csv(
            r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\9grocery\item_to_id.csv")
        historyDF = pd.read_csv(
            r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\9grocery\purchase_history.csv")
        historyDF_2 = self.reformatHistoryDF(historyDF)
        itemsDF["Item_id"] = itemsDF["Item_id"].astype(str)
        self.df = pd.merge(historyDF_2, itemsDF, on="Item_id", how="left")

    def reformatHistoryDF(self, historyDF):
        # Enclose multiple values in a col in []; given a array_string "he,wo" convert to ["he,"wo"] by splitting on ","
        historyDF["id"] = historyDF["id"].str.split(",")
        # convert the list to 1 col
        historyDF_unstacked = pd.DataFrame(
            historyDF["id"].apply(lambda x: pd.Series(x)).unstack().reset_index(level=0, drop=True))
        # join with orig to get other cols
        historyDF_2 = historyDF.join(historyDF_unstacked)
        # drop NA's from unstacking and joining
        historyDF_2.dropna(how='any', inplace=True)
        # drop the multi valued col
        historyDF_2 = historyDF_2.drop(labels="id", axis=1)
        historyDF_2.columns = ["User_id", "Item_id"]
        return historyDF_2

    def describeDF(self, df):
        print("HEAD: \n", df.head())
        print("DTYPES: \n", df.dtypes)
        print("SHAPE: \n", df.shape)

    def a1(self):
        df = self.df.copy()
        # gby for each user, select the items and count them
        df = df.groupby("User_id")["Item_id"].count().reset_index()
        df.columns = ["user_id", "count"]
        print(df.sort_values(by="count", ascending=False))

    def a2(self):
        df = self.df.copy()
        # for each item and user, select user and count them
        # dont confuse with counting users for each item
        df = df.groupby(["Item_id", "User_id"])["User_id"].agg({"userCount": "count"}).reset_index()
        # sort the df by item_id in asc and userCount in desc
        df = df.sort_values(by=["Item_id", "userCount"], ascending=[True, False])
        print(df.head())

    # def tsne1(self):
    #     seed = 5
    #     tsne = TSNE(random_state=seed)
    #     df=self.df.loc[:100000,["User_id","Item_id"]].copy()
    #     print(df.shape)
    #     for i in ["User_id","Item_id"]:
    #         df[i] = df[i].astype(int)
    #     print(df.values)
    #     tsneFit = tsne.fit_transform(df.values)
    #     plt.figure(figsize=(10, 10))
    #     # plt.title("digits classificationo using TSNE")
    #     # plt.xlim(tsneFit[:, 0].min(), tsneFit[:, 0].max() + 1)
    #     # plt.ylim(tsneFit[:, 1].min(), tsneFit[:, 1].max() + 1)
    #     # colors = ["#476A2A", "#7851B8", "#BD3430", "#4A2D4E", "#875525", "#A83683", "#4E655E", "#853541", "#3A3120",
    #     #           "#535D8E"]
    #     # # for i in range(len(self.df)):
    #     # #     # actually plot the digits as text instead of using scatter
    #     # #     # plt.text(tsneFit[i, 0], tsneFit[i, 1],), color=colors[digits.target[i]], fontdict={'weight': 'bold', 'size': 9})
    #     # #     plt.ylabel("t-SNE feature 0")
    #     # #     plt.xlabel("t-SNE feature 1")
    #
    #     plt.scatter(tsneFit[:,0],tsneFit[:,1])
    #     plt.show()

    def clusterItems(self):
        df = self.df.copy()
        df["bought"] = 1
        df2 = df.pivot_table(index=['User_id'], columns=['Item_name'], values=['bought'])
        df2.fillna(0, inplace=True)
        df3 = df2.ix[:, 1:49]
        self.corrDF = pd.DataFrame(df3.corr())


if __name__ == "__main__":
    s = Solution()
    s.loadData()
    s.describeDF(s.df)
    # s.a1()
    # s.a2()
    # s.tsne1()
    s.clusterItems()
