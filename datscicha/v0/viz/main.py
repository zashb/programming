import pandas as pd
import numpy as np
import logging

import matplotlib.pyplot as plt

plt.style.use('ggplot')


def loadDF(filenames):
    df_usr, df_tst = pd.read_csv(filenames[0]), pd.read_csv(filenames[1])
    for i in [df_usr, df_tst]:
        i["user_id"] = i["user_id"].astype(str).str.strip()
    df = pd.merge(df_tst, df_usr, on=["user_id"], how="left")
    logging.info(df.head())
    return df


def plot(df):
    df["age"] = df["age"].fillna(0)
    df["age"] = df["age"].astype(int)
    for i in ["age", "country", "sex", "browser", "device", "browser_language", "ads_channel", "source"]:
        df.groupby([i])["user_id"].agg({"#usrs": "count"}).plot(kind="bar")
        plt.title("#usrs for {}".format(i))
        plt.tight_layout()
        plt.show()
    return


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    df = loadDF([r"/home/bhargav/PythonWorkspace/bitB/datscicha/2spanistTTest/data/user_table.csv",
                 r"/home/bhargav/PythonWorkspace/bitB/datscicha/2spanistTTest/data/test_table.csv"])
    plot(df)
