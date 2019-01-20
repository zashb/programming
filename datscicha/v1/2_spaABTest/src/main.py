import pandas as pd
import numpy as np

from logging import *

getLogger().setLevel(INFO)
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind


def loadData(dict_files):
    dict_df = {}
    for i in dict_files:
        dict_df["df_" + i] = pd.read_csv(dict_files[i])
    # for i in dict_df:
    #     info(i)
    #     for j in [dict_df[i].head(), dict_df[i].shape, dict_df[i].dtypes]:
    #         info(j)
    df = pd.merge(dict_df["df_tt"], dict_df["df_ut"], on=["user_id"])
    return df


def descDF(df):
    dict_desc = {"head": df.head(), "shape": df.shape, "dtypes": df.dtypes}
    for i in dict_desc:
        info(i)
        info(dict_desc[i])
    return


def plotDist(df):
    for i in df.columns:
        if i not in ["conversion", "user_id", "date"]:
            df.groupby([i]).agg({"conversion": "mean"}).plot(kind="bar", legend=True)
            plt.ylabel("mean_conversion")
            plt.tight_layout()
            plt.show()
    return


def plotDist_time(df):
    df["date"] = pd.to_datetime(df["date"]).dt.date
    for i in ["source", "device", "browser_language", "ads_channel", "browser", "sex", "country"]:
        df_gby = pd.DataFrame(df.groupby(["date", i]).agg({"conversion": "mean"})).reset_index()
        # info(df_gby)
        fig = plt.figure()
        for j in df_gby[i].unique():
            df_j = df_gby.loc[df_gby[i] == j, ["date", "conversion"]]
            plt.plot(df_j["date"], df_j["conversion"], label=j)
        plt.title(i)
        plt.legend(loc="best")
        plt.tight_layout()
        plt.show()
    return


def ttest(df):
    # TODO: preprocess df before welch's ttest
    df_test = df.loc[df["country"] != "Spain", :]
    a, b = df_test.loc[df_test["test"] == 1, :], df_test.loc[df_test["test"] == 0, :]
    t, p = ttest_ind(a, b, equal_var=False)
    info("t: {}, p: {}".format(t, p))
    return


if __name__ == "__main__":
    dict_files = {"ut": r"/home/bhargav/PythonWorkspace/bitB/datscicha/v1/2spaABTest/data/user_table.csv",
                  "tt": r"/home/bhargav/PythonWorkspace/bitB/datscicha/v1/2spaABTest/data/test_table.csv"}
    df = loadData(dict_files)
    # descDF(df)
    # plotDist(df)
    # plotDist_time(df)
    ttest(df)


    # notes:
    # plot multiple timeseries on same plot
    # extract only date part from datetime col
