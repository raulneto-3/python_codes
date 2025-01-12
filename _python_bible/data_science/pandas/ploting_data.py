import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Anna', 'Bob', 'Charles','Daniel', 'Evan', 'Fiona','Gerald', 'Henry', 'India'],
        'Age': [24,24,35,45,22,54,54,43,25],
        'Height': [176,187,175,182,176,189,165,187,167]}
df = pd.DataFrame(data)
df.sort_values(by=['Age', 'Height'])
df.hist()
plt.show()

df.plot()
plt.show()

plt.plot(df['Age'], 'bo')
plt.show()
