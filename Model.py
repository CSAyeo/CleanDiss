import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler


def BuildModel(InitalTrainingSet,X_Train, Y_Train, DropoutRate, NodeCount, LayerCount):
    regressor = Sequential()
    # Adding the first LSTM layer and some Dropout regularisation
    regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_Train.shape[1], 1)))
    regressor.add(Dropout(0.2))
    print(NodeCount)
    for x in range(LayerCount):
        regressor.add(LSTM(units = NodeCount, return_sequences = True))
        regressor.add(Dropout(DropoutRate))
    regressor.add(LSTM(units = NodeCount))
    regressor.add(Dropout(DropoutRate))
    regressor.add(Dense(units = 1))
    # Compiling the RNN
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    # Fitting the RNN to the Training set
    regressor.fit(X_Train, Y_Train, epochs = 100, batch_size = 32)

    #Results============================================================

    dataset_test = pd.read_csv('TestData.csv')
    Real_Guardrail = dataset_test.iloc[:, 1:2].values
    # Getting the predicted stock price of 2017
    dataset_total = pd.concat((InitalTrainingSet['Start'], dataset_test['Start']), axis = 0)
    inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
    inputs = inputs.reshape(-1,1)
    Scaler = MinMaxScaler(feature_range = (0, 1))
    inputs = Scaler.fit_transform(inputs)
    X_test = []
    for i in range(60, 80):
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    Predicted_Guardrail = regressor.predict(X_test)
    Predicted_Guardrail = Scaler.inverse_transform(Predicted_Guardrail)

    return(Real_Guardrail ,Predicted_Guardrail)

