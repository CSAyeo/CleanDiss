from Model import *
from DataSimulator import *
from DataHandler import *
from DataVisualiser import *
from tensorflow import keras

setTrain(Dec(200),3)


x=0
InitalTrainingSet = pd.read_csv('TrainData3.csv'.format(x))#load the values
TrainSet = InitalTrainingSet.iloc[:, 1:2].values#select our values to use
print(TrainSet)
TrainScaled = Scaling(TrainSet)
print(TrainScaled)
SetX, SetY = TrainingStruct(TrainScaled)
print(f"{SetX=} \n {SetY=}")
Predict, Real = BuildModel(InitalTrainingSet, SetX, SetY)
PlotCurrentData(Real, Predict)
