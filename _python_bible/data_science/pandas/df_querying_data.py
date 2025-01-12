import pandas as pd

df = {'Name': ['Anna', 'Bob', 'Charles','Daniel', 'Evan', 'Fiona','Gerald', 'Henry', 'India'],
        'Age': [24,32,35,45,22,54,55,43,25],
        'Height': [176,187,175,182,176,189,165,187,167]}

print(df.loc[(df['Age'] == 24) & (df['Height'] > 180)])
print(df.loc[df['Age'] > 30]['Name'])