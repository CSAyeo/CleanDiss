from Model import *
from DataSimulator import *
from DataHandler import *
from DataVisualiser import *
from tensorflow import keras
setTrain(Inc(200))
import numpy as np

AveragePerformance = []
DropRate = np.arange(0, 1, 0.1)
LayerCount = np.arange(1, 10, 1)
NodeCount = np.arange(10, 100, 10)
print(f"{DropRate=} \n {LayerCount=} \n {NodeCount=}")
for DR in DropRate:
    for NC in NodeCount:
        for LC in LayerCount:
            ModelPerformance = []
            for x in range(10):
                print(f"{DR=} {NC=} {LC=}")
                Accuracy = []
                InitalTrainingSet = pd.read_csv('TrainData.csv')#load the values
                TrainSet = InitalTrainingSet.iloc[:, 1:2].values#select our values to use
                TrainScaled = Scaling(TrainSet)
                SetX, SetY = TrainingStruct(TrainScaled)
                Predict, Real = BuildModel(InitalTrainingSet, SetX, SetY, DR, NC, LC)
                for list1_i, list2_i in zip(Predict, Real):
                    Accuracy.append(list1_i-list2_i)
                ModelPerformance.append(sum(Accuracy) / len(Accuracy))
                print(ModelPerformance)
            AveragePerformance.append(sum(ModelPerformance) / len(ModelPerformance))
input("Finished: {}".format(AveragePerformance))
print(f"{AveragePerformance=}")
