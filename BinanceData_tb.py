from BinanceData import BinanceData

testRun = BinanceData('ETHUSDT', '15m', '2018.11.01 00:00:00', '2018.11.03 00:00:00')

# get api data:
pricesList = testRun.get_price_list()
_time = testRun.get_time()

print(pricesList['Open'].to_numpy(), _time)
