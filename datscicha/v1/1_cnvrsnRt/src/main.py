import pandas as pd
import numpy as np

from logging import *

getLogger().setLevel(INFO)
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier


def loadData(filename):
    df = pd.read_csv(filename)
    return df


def descDF(df):
    dict_desc = {"head": df.head(), "shape": df.shape, "dtypes": df.dtypes}
    for i in dict_desc:
        info(i)
        info(dict_desc[i])
    return


def plotDist(df):
    for i in df.columns:
        if i not in ["converted"]:
            df.groupby([i]).agg({"converted": "mean"}).plot(kind="bar", legend=True)
            plt.ylabel("mean_conversion")
            plt.tight_layout()
            plt.show()
    return


def plotCorr(df):
    cols_int = [i for i in df.columns if df[i].dtypes == "int64"]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(df.corr())
    fig.colorbar(cax)
    ax.set_xticklabels([""] + cols_int)
    ax.set_yticklabels([""] + cols_int)
    plt.tight_layout()
    plt.show()
    return


def prepDF(df):
    for i in ["country", "new_user", "source"]:
        df[i] = df[i].astype("category")
    # info(df.dtypes)
    cols_dummy = [i for i in df.columns if df[i].dtype.name == "category" and i not in ["converted"]]
    df = pd.get_dummies(df, columns=cols_dummy)
    lb = LabelBinarizer()
    df["converted"] = lb.fit_transform(df["converted"])
    info(df.shape)
    info(df.dtypes)
    df_prep = df.copy()
    return df_prep


def fitCv(df, seed):
    estimator = RandomForestClassifier(n_estimators=50, random_state=seed, n_jobs=-1)
    kfold = StratifiedKFold(n_splits=5, random_state=seed)
    Xcols = [i for i in df.columns if i not in ["converted"]]
    X, y = df.loc[:, Xcols], df.loc[:, "converted"]
    cvscores = cross_val_score(estimator=estimator, X=X, y=y, cv=kfold, scoring="accuracy", n_jobs=-1)
    info("mean cv score:")
    info(cvscores.mean())
    return


def fitEstimator(df, seed):
    Xcols = [i for i in df.columns if i not in ["converted"]]
    X, y = df.loc[:, Xcols], df.loc[:, "converted"]
    estimator = RandomForestClassifier(n_estimators=50, random_state=seed, n_jobs=-1)
    estimator.fit(X=X, y=y)
    # info(pd.DataFrame({"feat": Xcols, "imp": estimator.feature_importances_}))
    df_featimp = pd.DataFrame({"feat": Xcols, "imp": estimator.feature_importances_})
    df_featimp.plot(kind="bar")
    plt.tight_layout()
    plt.show()
    return estimator


if __name__ == "__main__":
    df = loadData(r"/home/bhargav/PythonWorkspace/bitB/datscicha/v1/1cnvrsnRt/data/conversion_data.csv")
    # descDF(df)
    # plotDist(df)
    # plotCorr(df)
    df_prep = prepDF(df)
    seed = np.random.seed(5)
    # fitCv(df_prep, seed)
    # estimator = fitEstimator(df_prep, seed)




# notes:
# new learnings:
# corr plot
# .dtype.name
# label binarizer
# X,y