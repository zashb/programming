import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.DEBUG)

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.tools as tls
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, plot

init_notebook_mode(connected=True)
tls.set_credentials_file(username="*****", api_key="*****")

from imblearn.under_sampling import RandomUnderSampler

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split


def loadData(filename):
    """
    # read data from file
    # show basic properties of the input dataset at a glance
    :param filename: absolute name of the data file
    :return: pd.DataFrame
    """
    logging.info("reading in data")
    # read data from file
    df = pd.read_csv(filename)
    # show basic properties of input dataset
    logging.info("properties of data at a glance:")
    logging.info("#rows:{}, #cols:{}".format(df.shape[0], df.shape[1]))
    logging.info("columns:{}".format(list(df.columns)))
    logging.info("#missing data points \n{}".format(df.isnull().sum()))
    return df


def cleanData(df):
    """
    # clean input data
    # create important features and/or flags
    # extract relevant features
    # answer question 1
    :param df: input dataframe
    :return: cleaned pd.DataFrame
    """
    logging.info("cleaning data...")
    # typecast columns to datetime
    for i in ["signup_date", "bgc_date", "vehicle_added_date"]:
        df[i] = pd.to_datetime(df[i])
    logging.info("typecasted array_string to datetime columns")
    # clean vehicle_year column
    df['vehicle_year'] = df['vehicle_year'].replace(to_replace=[0], value=np.NaN)
    logging.info("cleaned vehicle year values")
    # create missing data flags for columns with missing values
    for i in ["signup_os", "bgc_date", "vehicle_added_date", "vehicle_make", "vehicle_model", "vehicle_year"]:
        col_notnull = i + "_exists"
        df[col_notnull] = df[i].notnull().astype("int")
    logging.info("created exists flags for columns with missing values")
    # handle missing dates
    for i in ["bgc_date", "vehicle_added_date"]:
        df[i] = df[i].fillna(value=pd.to_datetime('1/1/2015'))
    logging.info("handled missing dates")
    # compute number of days between each of the major steps in the process
    df["days_signupToBgc"] = (df["bgc_date"] - df["signup_date"]).dt.days
    df["days_signupToVehicleAdd"] = (df["vehicle_added_date"] - df["signup_date"]).dt.days
    df["days_bgcToVehicleAdd"] = (df["vehicle_added_date"] - df["bgc_date"]).dt.days
    logging.info("created #days between signup_date,bgc_date and vehicle_added_date")
    # number of days cannot be negative
    for i in ["days_signupToBgc", "days_signupToVehicleAdd", "days_bgcToVehicleAdd"]:
        df[i] = df[i].clip(lower=0)
    logging.info("clipped days to min of 0")
    # extract day,month,year,week features from "signup_date", "bgc_date", "vehicle_added_date"
    for i in ["signup_date", "bgc_date", "vehicle_added_date"]:
        i_day, i_month, i_year, i_week = i + "_day", i + "_month", i + "_year", i + "_week"
        df[i_day] = df[i].dt.day
        df[i_month] = df[i].dt.month
        df[i_year] = df[i].dt.year
        #         df[i_week] = pd.Series(df[i].dt.strftime("%U").astype(int)+1).astype(str)
        df[i_week] = df[i].dt.strftime("%U")
    # extract year_week features for "signup_date", "bgc_date", "vehicle_added_date"
    df["signup_year_week"] = df["signup_date_year"].astype(str) + df["signup_date_week"].astype(str)
    df["bgc_year_week"] = df["bgc_date_year"].astype(str) + df["bgc_date_week"].astype(str)
    df["vehicle_added_year_week"] = df["vehicle_added_date_year"].astype(str) + df["vehicle_added_date_week"].astype(
        str)
    logging.info("extracted datetime features")
    # create tookFirstTrip feature
    df["tookFirstTrip"] = df["first_completed_date"].notnull().astype("int")
    logging.info("created took first trip flag")
    # answer question 1
    logging.info("{0:.2f}% of drivers took at a first trip".format(df["tookFirstTrip"].sum() * 100 / df.shape[0]))
    logging.info(df.isnull().sum())
    return df


def plotTookFirstTripDistribution(df_cleaned):
    logging.info("plotting took first trip distribution")
    ax = df_cleaned["tookFirstTrip"].value_counts().plot(kind="bar",
                                                         title="distribution of driver signups taking a first trip")
    ax.set_ylabel("#driver signups")
    ax.set_xticklabels(["didnot take first trip", "took first trip"])
    plt.show()
    return


def plotNumberOfDaysWithDriverSignupsTakingFirstTrip(df_cleaned):
    for i in ['days_signupToBgc', 'days_signupToVehicleAdd', 'days_bgcToVehicleAdd']:
        ax = df_cleaned.groupby(df_cleaned["tookFirstTrip"]).agg({i: "mean"}).plot(
            kind="bar", legend=False,
            title="Number of days between signup,bgc,vehicle_add against driver signups taking first trip")
        ax.set_ylabel("mean {}".format(i))
    plt.show()
    return


def plotCorr(df_cleaned):
    logging.info("plotting linear correlations")
    cols = [i for i in df_cleaned.columns if i not in ["id"]]
    corr = df_cleaned.loc[:, cols].corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr, cmap=sns.diverging_palette(200, 10, as_cmap=True), mask=mask)
    plt.title("linear correlation plot for cleaned driver signup dataset")
    plt.show()
    return


def plotYDist(df_cleaned):
    logging.info(
        "plotting distribution of driver signups who took first trip across days, signup_channel,signup_os,city_name")
    barCols = ["days_signupToBgc", "days_signupToVehicleAdd", "days_bgcToVehicleAdd", "signup_channel", "signup_os",
               "city_name"]
    fig = tls.make_subplots(rows=len(barCols), cols=1)
    x = 1
    for i in barCols:
        df_gby = pd.DataFrame(df_cleaned.groupby(i).agg({"tookFirstTrip": "mean"}).reset_index())
        trace = Bar(x=df_gby[i], y=df_gby["tookFirstTrip"], name=i)
        fig.append_trace(trace, x, 1)
        x += 1
    fig['layout'].update(title='Distributions of driverSignups who took first trip')
    plot(fig)
    return


def plotVariationOfNumOfdriverSignupsWhoTookFirstTripAcrossWeeks(df_cleaned):
    logging.info("plotting distribution of number of driver signups who took first trip across different weeks")
    for i in ["signup_year_week", "bgc_year_week", "vehicle_added_year_week"]:
        df_cleaned[i] = df_cleaned[i].astype('str')
        ax = df_cleaned.groupby([i]).agg({"tookFirstTrip": "mean"}).plot(legend=False,
                                                                         title="Variation of #driverSignups who took first trip across weeks for {}".format(
                                                                             i))
        ax.set_ylabel("mean #driverSignups who took first trip")
    plt.show()
    return


def exploreData(df_cleaned):
    logging.info("exploring data")
    plotTookFirstTripDistribution(df_cleaned)
    plotNumberOfDaysWithDriverSignupsTakingFirstTrip(df_cleaned)
    plotCorr(df_cleaned)
    # commented because this part requires plotly(open-source) credentials. pls find this viz in the .html version or .pdf version
    # plotYDist(df_cleaned)
    plotVariationOfNumOfdriverSignupsWhoTookFirstTripAcrossWeeks(df_cleaned)
    return


def prepData(df_cleaned):
    """
    prep dataframe to input to machine learning model
    :param df_cleaned: cleaned dataframe
    :return: cleaned and prepped pd.DataFrame
    """
    logging.info("prepping data for fitting machine learning models")
    list_dummCols = [i for i in df_cleaned.columns if df_cleaned[i].dtype.name == "object" and
                     i not in ["first_completed_date"]]
    df_cleaned_prepped = pd.get_dummies(df_cleaned, columns=list_dummCols)
    logging.info("created dummies for categorical columns")
    list_excludeCols = [i for i in df_cleaned_prepped.columns if i not in ["id", "first_completed_date", "signup_date",
                                                                           "bgc_date", "vehicle_added_date",
                                                                           "vehicle_year"]]
    df_cleaned_prepped = df_cleaned_prepped.loc[:, list_excludeCols]
    return df_cleaned_prepped


def balanceClasses(df_cleaned_prepped, seed):
    """
    handle class imbalance problem
    :param df_cleaned_prepped: cleaned and prepped dataframe
    :return: cleaned,prepped and balanced pd.DataFrame
    """
    logging.info("handling class imbalance problem")
    us = RandomUnderSampler(ratio=0.5, random_state=seed)
    X = df_cleaned_prepped.drop("tookFirstTrip", axis=1)
    y = df_cleaned_prepped["tookFirstTrip"]
    X_bal, y_bal = us.fit_sample(X, y)
    logging.info("undersampled not_taken_first_trip class randomly")
    logging.info("dimensions of df_cleaned_prepped:{}".format(df_cleaned_prepped.shape))
    X_bal_df = pd.DataFrame(X_bal, columns=X.columns)
    X_bal_df["tookFirstTrip"] = pd.Series(y_bal)
    logging.info("dimensions of df_cleaned_prepped_balanced:{}".format(X_bal_df.shape))
    logging.info(pd.Series(y).value_counts())
    logging.info(pd.Series(y_bal).value_counts())
    return X_bal_df


def crossValidateModel(df_cleaned_prepped_balanced, seed):
    """
    cross validate and measure generalization of the model
    :param df_cleaned_prepped_balanced: cleaned,prepped and balanced dataframe
    """
    logging.info(
        "assessing how well the Logistic Regression model generalizes using 5-Fold Stratified Cross Validation")
    estimator = LogisticRegression(n_jobs=-1, C=1.0)
    kfold = StratifiedKFold(n_splits=5, random_state=seed)
    X, y = df_cleaned_prepped_balanced.drop("tookFirstTrip", axis=1), df_cleaned_prepped_balanced["tookFirstTrip"]
    for i in ["accuracy", "f1_macro"]:
        cvscores = cross_val_score(estimator=estimator, X=X, y=y, cv=kfold, scoring=i, n_jobs=-1)
        logging.info("mean cv {0}:{1}".format(i, cvscores.mean()))
    return


def predictTookFirstTrip(df_cleaned_prepped_balanced, seed):
    """
    predict if a driver signup would take first trip
    :param df_cleaned_prepped_balanced: cleaned,prepped and balanced dataframe
    :param seed: random seed to reproduce results
    :return: estimator,prediction_probability,confusion matrix, classification report, accuracy
    """
    logging.info("assessing the predictive power of the model")
    X, y = df_cleaned_prepped_balanced.drop("tookFirstTrip", axis=1), df_cleaned_prepped_balanced["tookFirstTrip"]
    logging.info("splitting into training and test sets")
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=seed)
    estimator = LogisticRegression(C=1.0)
    logging.info("fitting the estimator")
    estimator.fit(X_train, y_train)
    logging.info("generating predictions")
    y_pred = estimator.predict(X_test)
    pred_prob = estimator.predict_proba(X_test)
    conf_mat = confusion_matrix(y_test, y_pred)
    logging.info("computing accuracy and classification report")
    class_rep = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info("plotting confusion matrix")
    df_confMat = pd.DataFrame(conf_mat, index=["tookFirstTrip", "didnotTakeFirstTrip"],
                              columns=["tookFirstTrip", "didnotTakeFirstTrip"])
    sns.heatmap(df_confMat, annot=True)
    plt.title("confusion matrix of drivers taking first trip")
    plt.show()
    TP, FP, FN, TN = conf_mat[0][0], conf_mat[0][1], conf_mat[1][0], conf_mat[1][1]
    logging.info("sensitivity:{}".format(TP / (TP + FN)))
    logging.info("specificity:{}".format(TN / (TN + FP)))
    logging.info("accuracy:{:.2f}".format(accuracy))
    logging.info("classification report: \n{}".format(class_rep))
    list_return = [estimator, pred_prob, conf_mat, class_rep, accuracy]
    return list_return


def main():
    df = loadData(r'...\ds_challenge_v2_1_data.csv')
    df_cleaned = cleanData(df)
    exploreData(df_cleaned)
    df_cleaned_prepped = prepData(df_cleaned)
    df_cleaned_prepped_balanced = balanceClasses(df_cleaned_prepped, 3)
    crossValidateModel(df_cleaned_prepped_balanced, 3)
    estimator, pred_prob, conf_mat, class_rep, accuracy = predictTookFirstTrip(df_cleaned_prepped_balanced, 3)
    return


if __name__ == '__main__':
    main()
