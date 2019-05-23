import logging
import math_prob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler


def readRawCsv(filename):
    df = pd.read_csv(filename)
    logging.info("read raw csv executed!")
    logging.info(df.head())
    return df


def prepData(df):
    df.columns = ["level1", "LVQ", "level2", "country", "date", "sla", "offered", "answered", "abandoned", "aht_s",
                  "wl_hs", "asa_s", "abandonRate", "avgAbandonTime_s"]
    for i in ["aht_s", "answered", "wl_hs"]:
        df[i] = df[i].astype(str)
        df[i] = df[i].str.replace(",", "")
        df[i] = df[i].str.replace("-", "0")
        df[i] = df[i].fillna("0")
        df[i] = df[i].astype(float)
    df_gaston = pd.read_csv(r"gaston_grps.csv")
    df = pd.merge(df, df_gaston, on="LVQ", how="left")
    df.gaston_region = df.gaston_region.fillna("Other")
    df["date"] = pd.to_datetime(df["date"])
    df["weekday"] = df.date.dt.dayofweek
    df = pd.DataFrame(df.groupby(["gaston_region", "LVQ", "date", "weekday"]).agg(
        {"wl_hs": "sum", "answered": "sum", "aht_s": "sum"})).reset_index()
    df = df.sort_values(["gaston_region", "LVQ", "date"], ascending=[True, True, True])
    logging.info(df[df.date >= "2017-05-09"].head())
    logging.info("prep data executed!")
    return df


def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)


def forecast_base(df, gr):
    np.random.seed(7)
    dataframe = pd.DataFrame(df.loc[df["gaston_region"] == gr, ["wl_hs"]])
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    train_size = int(len(dataset) * 0.85)
    train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
    look_back = 7
    trainX, trainY = create_dataset(train, look_back)
    testX = []
    for i in range(len(test) - look_back - 1):
        # a = test[i:(i + look_back), 0]
        a = np.array(np.repeat(i,7))
        testX.append(a)
        logging.info(type(a))
        logging.info(a)
    testX = np.array(testX)
    logging.info(type(testX))
    logging.info("testX")
    logging.info(testX)
    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=5, batch_size=1, verbose=2)
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    trainScore = math_prob.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    trainPredictPlot = np.empty_like(dataset)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict
    testPredictPlot = np.empty_like(dataset)
    testPredictPlot[:, :] = np.nan
    testPredictPlot[len(trainPredict) + (look_back * 2) + 1:len(dataset) - 1, :] = testPredict
    plt.plot(scaler.inverse_transform(dataset))
    plt.plot(trainPredictPlot)
    plt.plot(testPredictPlot)
    plt.show()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    # df = readRawCsv("2fe5c11a20114c8f8279ec44d4fd6db7.csv")
    # df_prep = prepData(df)
    # df_prep.to_pickle("df_prep.pkl")
    df_prep = pd.read_pickle("df_prep.pkl")
    forecast_base(df_prep, "AMERICA")
