import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(10,2),
                    index=[1,5,3,6,7,2,8,9,0,4],
                    columns=['A','B'])

print(df.sort_index())
print(df.sort_index(inplace=True))

data = {'Name': ['Anna', 'Bob', 'Charles','Daniel', 'Evan', 'Fiona','Gerald', 'Henry', 'India'],
        'Age': [24,24,35,45,22,54,54,43,25],
        'Height': [176,187,175,182,176,189,165,187,167]}

df = pd.DataFrame(data)

df.sort_values(by=['Age', 'Height'], inplace=True)

print(df)