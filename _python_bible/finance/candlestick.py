from matplotlib import pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from binance.client import Client
import datetime as dt

import pandas as pd


client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines_btc = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
btc = pd.DataFrame(klines_btc, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
btc = btc[['Date', 'Open', 'High', 'Low', 'Close']]
btc[['Open', 'High', 'Low', 'Close']] = btc[['Open', 'High', 'Low', 'Close']].astype(float)
# btc['Date'] = btc['Date'].map(mdates.date2num)

# ax = plt.subplot()
# candlestick_ohlc(ax, btc.values, width=2, colorup='g')
# ax.grid()
# ax.xaxis_date()
# plt.show()


import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=btc['Date'],
                                     open=btc['Open'],
                                     high=btc['High'],
                                     low=btc['Low'],
                                     close=btc['Close'])])

fig.update_layout(title='BTCUSDT Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)

fig.show()