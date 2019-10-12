
from BinanceData import BinanceData
from DataSetGenerator import DataSetGenerator

<<<<<<< HEAD
import os

import numpy as np
import pandas as pd



=======
>>>>>>> 122bdfedfa3b9c93cf43e38bbab06eb56641b42c
testRun = BinanceData('ETHUSDT',
                      '15m',
                       '2018.11.01 00:00:00',
                       '2018.11.01 1:00:00')


'''
matrix = np.random.randint(100, size=(3, 4))

d = DataSetGenerator(matrix, ['a', 'b', 'c', 'd']).write_data("test")

print(matrix)

test = pd.read_csv("../CSVFile/test.csv")


'''


x = np.array([testRun.get_price_list()['Open'].to_numpy(), testRun.get_price_list()['Close'].to_numpy()])
print(np.shape(x))


d = DataSetGenerator(x, np.array(range(5))).write_data("test")

t = pd.read_csv("../CSVFile/test.csv")

print(t['0'])

#x = np.concatenate((testRun.get_price_list()['Open'].to_numpy(),
                    #testRun.get_price_list()['Close'].to_numpy()))



