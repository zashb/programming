import numpy as np
import pandas as pd

from plotly.graph_objs import *
import cufflinks as cf
from plotly.offline import plot

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class Solution:
    def __init__(self):
        self.seed = 5
        self.df = pd.DataFrame()
        self.df_clean = pd.DataFrame()

    def main(self):
        # load data
        self.df = self.loadData("song.json")
        # clean df
        self.df_clean = self.cleanDF(self.df.copy())
        # extract DT feats
        self.df_clean = self.extractDTFeats(self.df_clean)

    def loadData(self, fileName):
        fileDir = r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\data\8songChal\\"
        df = pd.read_json(fileDir + fileName)
        return df

    def describeDF(self, df):
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)
        print("DTYPE COUNTS : \n", df.get_dtype_counts())
        print("DTYPES : \n", df.dtypes)

    def cleanDF(self, df):
        # strip colnames
        df.columns = [i.strip() for i in df.columns]
        # convert to dt
        df["time_played"] = pd.to_datetime(df["time_played"], format="%Y-%m-%d %H:%M:%S")
        df["user_sign_up_date"] = pd.to_datetime(df["user_sign_up_date"], format="%Y-%m-%d")
        # strip obj columns
        for i in df.columns:
            if df[i].dtypes == "object":
                df[i] = df[i].str.strip()

        return df

    def countUnique(self, df):
        for col in df.columns:
            uniqueVals = df[col].unique()
            print("# UNIQUE VALS IN {0} : \n {1}".format(col, len(uniqueVals)))
            if len(uniqueVals) < 10:
                print("VALUE COUNTS : \n", df[col].value_counts(dropna=False))
            else:
                print("TOO MANY UNIQUES")

    def q1(self, df):
        # gby state, cnt user_id
        usrCnt = df.groupby(["user_state"], as_index=False).agg({"user_id": "count"})
        usrCnt.sort_values(by=["user_id"], ascending=False, inplace=True)
        top3 = usrCnt["user_state"].head(3)
        bottom3 = usrCnt["user_state"].tail(3)
        print("TOP 3 STATES WRT #USERS : \n", top3)
        print("BOTTOM 3 STATES WRT #USERS : \n", bottom3)

    def extractDTFeats(self, df):
        # conv to str
        df["time_played"] = df["time_played"].astype(str)
        # rem this for life
        df["date"], df["time"] = zip(*df["time_played"].str.split())
        df = df.drop(["time_played"], axis=1)
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
        df["day"] = df["date"].dt.day
        df["month"] = df["date"].dt.month
        df["year"] = df["date"].dt.year
        df["hour"], df["minute"], df["second"] = zip(*df["time"].str.split(":"))
        return df

    def q2(self, df):
        # users visiting site on more #days
        dayCnt = df.groupby(["user_id"], as_index=False).agg({"day": "count"})
        dayCnt.columns = ["user_id", "userdays"]
        # user id state mapping
        usrIdState = df.groupby(["user_id", "user_state"], as_index=False).agg({"day": "count"})
        # join above 2
        merged = pd.merge(dayCnt, usrIdState, how="left", on=["user_id"])
        merged.sort_values(["userdays"], ascending=False, inplace=True)
        print("TOP 3 STATES WRT #DAYS : \n", merged["user_state"].unique()[:3])
        print("BOTTOM 3 STATES WRT #DAYS : \n", merged["user_state"].unique()[::-1][:3])

    def q3(self, df):
        gbyStateDate = df.groupby(["user_state"]).agg({"user_sign_up_date": min}).reset_index()
        getUser = df.loc[:, ["user_id", "user_state", "user_sign_up_date"]]
        firstUserState = pd.merge(gbyStateDate, getUser, how="left",
                                  on=["user_state", "user_sign_up_date"]).drop_duplicates(keep="first")
        print(firstUserState,"\n",firstUserState.shape)


if __name__ == "__main__":
    s = Solution()
    s.main()
    # s.describeDF(s.df_clean)
    # s.countUnique(s.df_clean)
    # s.q1(s.df_clean)
    # s.q2(s.df_clean)
    # s.q2(s.df_clean)
    s.q3(s.df_clean)
