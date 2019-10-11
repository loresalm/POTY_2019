from binance.client import Client
import pandas as pd
"""@package docstring
Documentation for this module.
More details.
"""


class BinanceData:

    client = Client("", "")
    coin = 0
    coin_tb = []
    time_tb = []
    priceList = [[]]
    time = []

    def __init__(self, _symbol, _interval, _start_str, _end_str):
        self.coin = self.client.get_historical_klines(symbol=_symbol,
                                                      interval=_interval,
                                                      start_str=_start_str,
                                                      end_str=_end_str)
        self.coin_tb = pd.DataFrame(self.coin,
                                    columns=['Open time',
                                             'Open',
                                             'High',
                                             'Low',
                                             'Close',
                                             'Volume',
                                             'Close time',
                                             'Quote asset volume',
                                             'Number of trades',
                                             'Taker buy base asset volume',
                                             'Taker buy quote asset volume',
                                             'Ignore'])

        self.time_tb = pd.to_datetime(self.coin_tb['Open time'], unit='ms')

        self.priceList= [['Open'],['High'],['Low'],['Close']]
        for i in range(0,4):
            self.priceList[i]= self.coin_tb[self.priceList[i][0]].astype(float)

        for i in range(0,len(self.time_tb)):
            self.time.append(i)

    def get_price_list(self):
        return self.priceList

    def get_time(self):
        return self.time


testRun = BinanceData('ETHUSDT',
                      '15m',
                       '2018.11.01 00:00:00',
                       '2018.11.03 00:00:00')

# get api data:
pricesList = testRun.get_price_list()
_time = testRun.get_time()

print(pricesList, _time)



