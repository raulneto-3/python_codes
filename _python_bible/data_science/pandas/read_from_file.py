import pandas as pd

data = {'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age': [24,24,35,45,22,54,54,43,25],
        'Height': [176,187,175,182,176, 189,165,187,167]}

df = pd.DataFrame(data)
df.to_csv('python_bible/data_science/pandas/data.csv', index=False)

data = pd.read_csv('python_bible/data_science/pandas/data.csv')
data.set_index('id', inplace=True)
print(data)
