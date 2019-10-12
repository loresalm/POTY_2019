
import SelectData
from BinanceData import BinanceData
from DataSetGenerator import DataSetGenerator
from SelectData import SelectData
import pandas as pd
import numpy as np

x = SelectData().api(['High', 'Low'],'ETHUSDT', '15m', '2018.11.01 00:00:00', '2018.11.03 00:00:00')

print((52359-147)/ 228)

print(x)

testRun = BinanceData('ETHUSDT',
                      '15m',
                       '2018.11.01 00:00:00',
                       '2018.11.01 1:00:00')



b1 = np.array([testRun.get_price_list()['Open'].to_numpy(), testRun.get_price_list()['Close'].to_numpy()])
print(np.shape(x))


b2 = DataSetGenerator(b1, np.array(range(5))).write_data("testSelectDasta")

b3 = SelectData().save(['0', '1'], "../CSVFile/testSelectDasta.csv")

print(b3)