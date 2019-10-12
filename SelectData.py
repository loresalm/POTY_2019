from BinanceData import BinanceData
import pandas as pd
import numpy as np


class SelectData:

    #_legend:  list of what price you want. { ex: x = ['Open', 'Close'] }

    def api(self, _legend, _symbol, _interval, _start_str, _end_str):

        data = BinanceData(_symbol, _interval, _start_str, _end_str)

        select_data = []
        for i in _legend:
            select_data.append(data.get_price_list()[i].to_numpy())

        return np.asarray(select_data, dtype= float)

    def save(self, _legend, _fileName):
        data = pd.read_csv(_fileName)
        select_data = []
        for i in _legend:
            select_data.append(data[i].to_numpy())

        return np.asarray(select_data, dtype= float)







