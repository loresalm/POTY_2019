from Display import Display
from SelectData import SelectData
from BinanceData import BinanceData
import numpy as np

# bin_dat = BinanceData('ETHUSDT', '15m', '2018.11.01 00:00:00', '2018.11.03 00:00:00')
# pricesList = bin_dat.get_price_list()

pricesList = SelectData().save(['Open', 'Close'], '../CSVFile/D_S_F_FiltredData.csv')


Open = np.array(pricesList[0])
Close = np.array(pricesList[1])
High = np.array(pricesList[0])
Low = np.array(pricesList[1])

data = np.array([Open, High, Low, Close])

print(len(data[0]))
display_test = Display()
display_test.load_data(data)
display_test.run_app()
