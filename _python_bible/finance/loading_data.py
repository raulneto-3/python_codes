from binance.client import Client
import datetime as dt
import pandas as pd

client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
df = pd.DataFrame(klines, columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
df.index = pd.to_datetime(df['timestamp'], unit='ms')
df = df[['Open', 'High', 'Low', 'Close']]
df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype(float)

print(df.head())

# Open: That's the price at which the stock opened trading on the day
# High: The highest price at which the stock traded during the day
# Low: The lowest price at which the stock traded during the day
# Close: The price at which the stock closed trading on the day
# Volume: How many shares were traded
# Adj Close: The closing price, adjusted for stock splits and dividends

print(df['Close'].head())
print(df['Close'][5])

# save data to csv
df.to_csv('finance/BTCUSDT.csv')
# save data to excel
df.to_excel('finance/BTCUSDT.xlsx')
# save data to html
df.to_html('finance/BTCUSDT.html')
# save data to json
df.to_json('finance/BTCUSDT.json')

# load data from csv
df = pd.read_csv('finance/BTCUSDT.csv')
# load data from excel
df = pd.read_excel('finance/BTCUSDT.xlsx')
# load data from html
df = pd.read_html('finance/BTCUSDT.html')
# load data from json
df = pd.read_json('finance/BTCUSDT.json')