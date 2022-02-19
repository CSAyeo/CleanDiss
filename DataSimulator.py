from random import random
import numpy as np


def Flat(Years):
    import numpy as np
    Start = 500
    StartList, EndList = [], []
    for Year in range(Years):
        TStart = Start / np.random.uniform(1, 1.2)
        End = TStart / np.random.uniform(0.9, 1.1)
        StartList.append(round(Start / np.random.uniform(1, 1.2)))
        EndList.append(round(TStart / np.random.uniform(0.9, 1.1)))
    import pandas as pd
    print(f"{StartList=}{EndList=}")
    YearRange = pd.date_range(start='1/1/2015', periods=Years, freq='A')
    df = pd.DataFrame(list(zip(StartList, EndList)), index = YearRange, columns=['Start', 'End'])
    print(df)

def Inc(Years):
    import numpy as np
    Start = 500
    StartList, EndList = [], []
    for Year in range(Years):
        Start = Start * np.random.uniform(1, 1.1)
        End = Start * np.random.uniform(0.9, 1.1)
        StartList.append(round(Start))
        EndList.append(round(End))
    import pandas as pd
    print(f"{StartList=}{EndList=}")
    YearRange = pd.date_range(start='1/1/2015', periods=Years, freq='A')
    df = pd.DataFrame(list(zip(StartList, EndList)), index = YearRange, columns=['Start', 'End'])
    print(df)

def Dec(Years):
    import numpy as np
    Start = 500
    StartList, EndList = [], []
    for Year in range(Years):
        Start = Start / np.random.uniform(1, 1.2)
        End = Start / np.random.uniform(0.9, 1.1)
        StartList.append(round(Start))
        EndList.append(round(End))
    import pandas as pd
    print(f"{StartList=}{EndList=}")
    YearRange = pd.date_range(start='1/1/2015', periods=Years, freq='A')
    df = pd.DataFrame(list(zip(StartList, EndList)), index = YearRange, columns=['Start', 'End'])
    print(df)


def Norm(Years):
    import numpy as np
    mean, stdev = 500, 5
    Years = 5
    #Iterate over startlist
    StartList = np.random.normal(mean, stdev, size=Years)
    StartList = [round(x) for x in StartList] #remove the decimal
    print(StartList)
    EndList = []
    for x in StartList:
        EndList.append(round(x / np.random.uniform(0.9, 1.1)))
    import pandas as pd
    YearRange = pd.date_range(start='1/1/2015', periods=Years, freq='A')
    df = pd.DataFrame(list(zip(StartList, EndList)), index = YearRange, columns=['Start', 'End'])
    print(df)

def Uniform(Years):
    import numpy as np
    mean, stdev = 500, 5
    Years = 5
    #Iterate over startlist
    StartList = np.random.uniform(mean, stdev, size=Years)
    StartList = [round(x) for x in StartList] #remove the decimal
    print(StartList)
    EndList = []
    for x in StartList:
        EndList.append(round(x / np.random.uniform(0.9, 1.1)))
    import pandas as pd
    YearRange = pd.date_range(start='1/1/2015', periods=Years, freq='A')
    df = pd.DataFrame(list(zip(StartList, EndList)), index = YearRange, columns=['Start', 'End'])
    print(df)

def setTest(df):
    print("Saving test...")
    df.to_csv("TestData.csv")

def setTrain(df):
    print("Saving training...")
    df.to_csv("TrainData.csv")
