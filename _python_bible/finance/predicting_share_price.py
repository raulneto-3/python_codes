from binance.client import Client
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import datetime as dt

client = Client("YrLjPE0nlg9I0wFFgILb94ThUEB831AYv5ejxaSJIrq2VnqYQ2ZiZTTCYISMMnEq", "UeY5ILuWljXISvDxWb7ftziE2LK0Gr0TyoUr01olopT6uJmjOFd334Y8hmhsCGNS")
klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2020')
df = pd.DataFrame(klines, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
df.index = pd.to_datetime(df['Date'], unit='ms')
df = df[['Open', 'High', 'Low', 'Close']]
df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype(float)
# data = df['Close']

days = 30
df['Shifted'] = df['Close'].shift(-days)
df.dropna(inplace=True)
X = np.array(df.drop(['Shifted'], axis=1))
Y = np.array(df['Shifted'])
X = preprocessing.scale(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# Train the model
clf = LinearRegression()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print(accuracy)

# Predict the future
X = X[:-days]
X_new = X[-days:]
print(X_new)
prediction = clf.predict(X_new)
print(prediction)
print(df.tail(days))

import plotly.graph_objects as go
import plotly.express as px

# Adicione a coluna 'Prediction' ao DataFrame
df['Prediction'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in prediction:
    next_date = dt.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

# Filtre o DataFrame para incluir apenas os últimos 300 dias
df_filtered = df.tail(300)

# Crie a figura com plotly
fig = go.Figure()

# Adicione a série temporal 'Close'
fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['Close'], mode='lines', name='Close'))

# Adicione a série temporal 'Prediction'
fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['Prediction'], mode='lines', name='Prediction'))

# Configure os rótulos e a legenda
fig.update_layout(
    title='Previsão de Preço das Ações',
    xaxis_title='Data',
    yaxis_title='Preço',
    legend=dict(x=0, y=1)
)

# Mostre a figura
fig.show()