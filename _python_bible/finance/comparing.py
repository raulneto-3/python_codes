from binance.client import Client
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines_btc = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
btc = pd.DataFrame(klines_btc, columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
btc.index = pd.to_datetime(btc['timestamp'], unit='ms')
btc = btc[['Open', 'High', 'Low', 'Close']]
btc[['Open', 'High', 'Low', 'Close']] = btc[['Open', 'High', 'Low', 'Close']].astype(float)

klines_eth = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
eth = pd.DataFrame(klines_eth, columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
eth.index = pd.to_datetime(eth['timestamp'], unit='ms')
eth = eth[['Open', 'High', 'Low', 'Close']]
eth[['Open', 'High', 'Low', 'Close']] = eth[['Open', 'High', 'Low', 'Close']].astype(float)


btc['Close'].plot(label='BTC')
eth['Close'].plot(label='ETH')
# style.use('ggplot')
# plt.ylabel('Price')
# plt.title('Stock Price')
# plt.legend(loc='upper left')
# plt.show()


# plt.subplot(211)
# btc['Close'].plot(label='BTC')
# plt.title('BTC Stock Price')
# plt.ylabel('Price')
# plt.subplot(212)
# eth['Close'].plot(label='ETH')
# plt.title('ETH Stock Price')
# plt.ylabel('Price')
# plt.show()

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('BTC Stock Price', 'ETH Stock Price'))

# Add BTC trace
fig.add_trace(go.Scatter(x=btc.index, y=btc['Close'], mode='lines', name='BTC'), row=1, col=1)

# Add ETH trace
fig.add_trace(go.Scatter(x=eth.index, y=eth['Close'], mode='lines', name='ETH'), row=2, col=1)

# Update layout
fig.update_layout(title='Stock Price', yaxis_title='Price', legend=dict(x=0, y=1.0), legend_traceorder='normal')

# Show plot
fig.show()