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

# import matplotlib.pyplot as plt

# df['Close'].plot()
# plt.show()

# from matplotlib import style
# style.use('ggplot')
# plt.ylabel('Price')
# plt.title('BTCUSDT Stock Price')
# df['Close'].plot()
# plt.show()


import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))

fig.update_layout(
    title='BTCUSDT Stock Price',
    yaxis_title='Price',
    template='ggplot2'
)

fig.show()