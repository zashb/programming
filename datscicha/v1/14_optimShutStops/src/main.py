import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from logging import *
getLogger().setLevel(INFO)

def loadData(filename):
    df = pd.read_csv(filename)
    return df

def descDF(df):
    dict_desc = {"head": df.head(), "shape": df.shape, "dtypes": df.dtypes}
    for i in dict_desc:
        print(i)
        print(dict_desc[i])
    return

if __name__ == '__main__':
    df_pbs,df_ea = loadData(r"C:\Users\sg0222350\My Stuff\learn\python\datscicha\v1\14_optimShutStops\dat\Potentail_Bust_Stops.csv"),loadData(r"C:\Users\sg0222350\My Stuff\learn\python\datscicha\v1\14_optimShutStops\dat\Employee_Addresses.csv")
    for i in [df_pbs,df_ea]:    descDF(i)