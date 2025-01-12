import pandas as pd

series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])

# Accessing elements in a series
print(series['A'])
print(series[0])

# Converting dictionary to series
myDic = {'A': 10, 'B': 20, 'C': 30}
series = pd.Series(myDic)
seriesB = pd.Series(myDic, index=['C','A','B'])


