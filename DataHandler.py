import ast

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def OneDimdt(df):
    j= df.iloc[:,0].tolist()
    return j

def firstport():
    alldata = pd.read_csv('TrainData.csv', index_col=0)
    print(alldata)
    portfolio = alldata.iloc[:, 0].values
    print(portfolio)
    t = portfolio[0]
    print(f"{t=}")
    x = ast.literal_eval(t)
    print(x)
    df = pd.DataFrame(x)
    print (df)
    return df

def Scaling(TrainSet):
    scaler = MinMaxScaler(feature_range = (0, 1))
    TrainScaled = scaler.fit_transform(TrainSet)
    return(TrainScaled)

def TrainingStruct(TrainScaled):
    X_Train = []
    Y_Train = []
    for i in range(60, len(TrainScaled)): #range (x,y)
        X_Train.append(TrainScaled[i-60:i, 0])
        Y_Train.append(TrainScaled[i, 0])
    X_Train, Y_Train = np.array(X_Train), np.array(Y_Train)
    return X_Train, Y_Train
