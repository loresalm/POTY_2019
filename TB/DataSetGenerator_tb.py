
from BinanceData import BinanceData
from DataSetGenerator import DataSetGenerator

import numpy as np
import pandas as pd

import math




testRun = BinanceData('ETHUSDT',
                      '5m',
                       '2018.12.01 00:00:00',
                       '2018.12.02 00:00:05')


''' 
matrix = np.random.randint(100, size=(3, 4))

d = DataSetGenerator(matrix, ['a', 'b', 'c', 'd']).write_data("testttt")

print(matrix)

test = pd.read_csv("../CSVFile/testttt.csv")

'''



x = np.array([testRun.get_price_list()['Open'].to_numpy(), testRun.get_price_list()['Close'].to_numpy()])
print(np.shape(x))


d = DataSetGenerator(x, np.array(range(5))).write_data("D_S_F_FiltredData")

t = pd.read_csv("../CSVFile/D_S_F_FiltredData.csv")

print(t['0'])





#d = DataSetGenerator(x.T, np.array(['Open', 'Close'])).write_data("dataSet(2018:06:01-2018:12:01)")


