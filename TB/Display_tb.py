from Display import Display
from BinanceData import BinanceData
import numpy as np

bin_dat = BinanceData('ETHUSDT', '15m', '2018.06.01 00:00:00', '2018.12.03 00:00:00')
pricesList = bin_dat.get_price_list()

Open = np.array(pricesList['Open'])
Close = np.array(pricesList['Close'])
High = np.array(pricesList['High'])
Low = np.array(pricesList['Low'])

data = np.array([Open, High, Low, Close])

print(len(data[0]))
display_test = Display()
display_test.load_data(data)
display_test.run_app()
