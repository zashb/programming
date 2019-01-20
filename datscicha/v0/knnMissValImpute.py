import pandas as pd
import numpy as np
from fancyimpute import KNN
import matplotlib.pyplot as plt


def imputeMissKNN():
    df = pd.DataFrame()
    df['x0'] = [0.3051, 0.4949, 0.6974, 0.3769, 0.2231, 0.341, 0.4436, 0.5897, 0.6308, 0.5]
    df['x1'] = [np.nan, 0.2654, 0.2615, 0.5846, 0.4615, 0.8308, 0.4962, 0.3269, 0.5346, 0.6731]
    print(df.head())
    X = df.as_matrix(columns=["x0", "x1"])
    print("X:\n", X)
    XImputed = KNN(k=3).complete(X)
    print("XImputed:\n", XImputed)


if __name__ == "__main__":
    imputeMissKNN()
