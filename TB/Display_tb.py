from Display import Display
from SelectData import SelectData
from BinanceData import BinanceData
import numpy as np

<<<<<<< HEAD
# bin_dat = BinanceData('ETHUSDT', '15m', '2018.11.01 00:00:00', '2018.11.03 00:00:00')
# pricesList = bin_dat.get_price_list()
=======
bin_dat = BinanceData('ETHUSDT', '15m', '2018.06.01 00:00:00', '2018.12.03 00:00:00')
pricesList = bin_dat.get_price_list()
>>>>>>> f1e7e09dd90b8dfc6a592fb868c630104aaa89c1

pricesList = SelectData().save(['Open', 'Close'], '../CSVFile/D_S_F_FiltredData.csv')

<<<<<<< HEAD

Open = np.array(pricesList[0])
Close = np.array(pricesList[1])
High = np.array(pricesList[0])
Low = np.array(pricesList[1])

data = np.array([Open, High, Low, Close])

=======
data = np.array([Open, High, Low, Close])

>>>>>>> f1e7e09dd90b8dfc6a592fb868c630104aaa89c1
print(len(data[0]))
display_test = Display()
display_test.load_data(data)
display_test.run_app()
