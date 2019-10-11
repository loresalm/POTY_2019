
from BinanceData import BinanceData
from DataSetGenerator import DataSetGenerator



testRun = BinanceData('ETHUSDT',
                      '15m',
                       '2018.11.01 00:00:00',
                       '2018.11.01 2:00:00')

x = testRun.get_price_list()

d = DataSetGenerator(x).write_data("test")