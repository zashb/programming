import logging

import matplotlib
import pandas as pd

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def main():
    filename = "/Users/bhargavayyagari/github/datscicha/v1/uber_dsc/ds_challenge_v2_1_data.csv"
    df = get_df(filename)
    get_first_trip_count(df)
    plot_took_first_trip_distribution(df)


def plot_took_first_trip_distribution(df):
    logging.info("plotting took first trip distribution")
    ax = df["took_first_trip"].value_counts().plot(kind="bar",
                                                   title="distribution of driver signups taking a first trip")
    ax.set_ylabel("#driver signups")
    ax.set_xticklabels(["didnot take first trip", "took first trip"])
    plt.tight_layout()
    plt.show()


def get_first_trip_count(df):
    logging.info("Getting first trip count")
    df["took_first_trip"] = df["first_completed_date"].notnull()
    first_trip_count = df["took_first_trip"].sum() * 100 / df.shape[0]
    logging.info("{:.2f} % of drivers took first trip".format(first_trip_count))


def get_df(filename: str) -> pd.DataFrame:
    logging.info("Getting dataframe")
    df = pd.read_csv(filename, sep="\t")
    logging.info("columns:{}".format(list(df.columns)))
    missing_val_count = df.isnull().sum()
    logging.info("missing val count: \n{}".format(missing_val_count))
    logging.info("column types : \n{}".format(df.dtypes))
    return df


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
