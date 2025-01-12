from binance.client import Client
import datetime as dt
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1WEEK, '1 Jan 2020')
df = pd.DataFrame(klines, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
df.index = pd.to_datetime(df['Date'], unit='ms')
df = df[['Open', 'High', 'Low', 'Close']]
df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype(float)



data = df['Close']
rstart = data.index[-50]
# rstart = data.index[-25]
# rstart = data.index[-5]
rend = data.index[-1]
fit_data = data.reset_index()
post1 = fit_data[fit_data['Date'] > rstart].index[0]
post2 = fit_data[fit_data['Date'] < rend].index[-1]
fit_data = fit_data.iloc[post1:post2]

dates = fit_data['Date'].map(mdates.date2num)
fit = np.polyfit(dates, fit_data['Close'], 1)
fitid = np.poly1d(fit)

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(fit_data['Date'], fitid(dates), 'r')
plt.show()