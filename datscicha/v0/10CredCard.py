import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotly.offline import plot
from plotly.graph_objs import *

from sklearn.manifold import TSNE


class ccFraud:
    def __init__(self):
        self.df = pd.DataFrame()

    def loadData(self):
        ccDF = pd.read_csv(
            r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\10ccFraud\cc_info.csv")
        transactionDF = pd.read_csv(
            r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\10ccFraud\transactions.csv")
        # left because transaction info is more imp and cc info is just a good to know
        self.df = pd.merge(transactionDF, ccDF, how="left", on="credit_card")

    def describeDF(self, df):
        print("HEAD: \n", df.head())
        print("SHAPE: \n", df.shape)
        print("DTYPES: \n", df.dtypes)

    def formatDF(self):
        df = self.df.copy()
        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day
        df["hour"] = df["date"].dt.hour
        df["minute"] = df["date"].dt.minute
        df["second"] = df["date"].dt.second
        df = df.drop(["date"], axis=1)
        df["credit_card"] = df["credit_card"].astype(str)
        df["credit_card_limit"] = df["credit_card_limit"].astype(int)
        self.df = df

    def a1(self):
        df = self.df.copy()
        # for each cc,year,month, total money
        df_monthlySpend = df.groupby(["credit_card", "year", "month"])["transaction_dollar_amount"].agg(
            {"totalUsage": "sum"}).reset_index()
        # join with orig to get monthly limit
        df_merged = pd.DataFrame(
            pd.merge(df_monthlySpend, df.loc[:, ["credit_card", "year", "month", "credit_card_limit"]],
                     how="left", on=["credit_card", "year", "month"]).drop_duplicates(keep="first"))
        # filter rows where usage <= cc limit
        df_merged_withinLimit = pd.DataFrame(df_merged.apply(
            lambda x: x[["credit_card", "totalUsage", "credit_card_limit"]] if x["totalUsage"] <= x[
                "credit_card_limit"] else None, axis=1))
        print(df_merged_withinLimit["credit_card"].unique())

    def a2(self, y, m, d):
        df = self.df.copy()
        # total usage for each day for a cc
        df_usage = df.groupby(["credit_card", "year", "month", "credit_card_limit", "day"])[
            "transaction_dollar_amount"].agg({"totalUsage": "sum"}).reset_index()
        # cumulative usage for every day in a month
        df_usage["cumUsage"] = df_usage.groupby(["credit_card", "year", "month", "credit_card_limit"])[
            "totalUsage"].cumsum()
        # df_usage = df_usage.groupby(["credit_card", "year", "month", "credit_card_limit"])["totalUsage"].agg(
        #     {"cumUsage": "cumsum"}).reset_index()
        print(df_usage.loc[(df_usage["cumUsage"] > df_usage["credit_card_limit"]) & (df_usage["year"] == y) & (
            df_usage["month"] == m) & (df_usage["day"] == d), :])
        print(df_usage.shape)
        print(df_usage.head())
        df_usage_tsne = df_usage.sample(n=10000)
        tsne = TSNE(random_state=5)
        tsneFit = tsne.fit_transform(df_usage_tsne)
        plt.figure(figsize=(10, 10))
        plt.scatter(tsneFit[:, 0], tsneFit[:, 1],c=df_usage_tsne["month"])
        plt.show()


if __name__ == "__main__":
    cc = ccFraud()
    cc.loadData()
    cc.formatDF()
    cc.describeDF(cc.df)
    # cc.a1()
    cc.a2(2015, 10, 24)
