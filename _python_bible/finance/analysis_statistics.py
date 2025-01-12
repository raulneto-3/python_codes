from binance.client import Client
import datetime as dt
from matplotlib import pyplot as plt
import pandas as pd

client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines = client.get_historical_klines('ZROUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
df = pd.DataFrame(klines, columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
df.index = pd.to_datetime(df['timestamp'], unit='ms')
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)

df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

print(df.head())


# ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
# ax1.plot(df.index, df['Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.fill_between(df.index, df['Volume'])
# plt.show()

import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'), 
                    row_width=[0.2, 0.7])

# Plot OHLC
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['100ma'], mode='lines', name='100 MA'), row=1, col=1)

# Plot Volume
fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'), row=2, col=1)

fig.update_layout(title='Historical Price and Volume', xaxis_title='Date', yaxis_title='Price', 
                  yaxis2_title='Volume', showlegend=False)

fig.show()


# PCT_change: Percentage change between the Close and Open prices
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100
# HL_PCT: Percentage change between the High and Low prices
df['HL_PCT'] = (df['High'] - df['Low']) / df['Low'] * 100
