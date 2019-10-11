from binance.client import Client
import pandas as pd
"""@package docstring
Documentation for this module.
More details.
"""


class BinanceData:

    def __init__(self, _symbol, _interval, _start_str, _end_str):

        self.symbol = _symbol
        self.interval = _interval
        self.start_str = _start_str
        self.end_str = _end_str

        self.time = []
        self.client = Client("", "")
        self.coin = []
        self.coin_data = []
        self.time_data = []

        self.update_data()

    def set_symbol(self, _symbol):
        self.symbol = _symbol
        self.update_data()

    def interval(self, _interval):
        self.interval = _interval
        self.update_data()

    def set_limits(self, _start_str, _end_str):
        self.start_str = _start_str
        self.end_str = _end_str
        self.update_data()

    def get_price_list(self):
        return self.coin_data

    def get_time(self):
        return self.time

    def update_data(self):
        self.coin = self.client.get_historical_klines(symbol=self.symbol,
                                                      interval=self.interval,
                                                      start_str=self.start_str,
                                                      end_str=self.end_str)
        self.coin_data = pd.DataFrame(self.coin,
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
        self.time_data = pd.to_datetime(self.coin_data['Open time'], unit='ms')





