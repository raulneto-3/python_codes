import pandas as pd
names = pd.DataFrame({
            'id': [1,2,3,4,5],
            'name': ['Anna', 'Bob', 'Charles',
            'Daniel', 'Evan'],
        })
ages = pd.DataFrame({
            'id': [1,2,3,4,5],
            'age': [20,30,40,50,60]
        })

df = pd.merge(names,ages,on='id')
df.set_index('id', inplace=True)

## Joins
# left - Use keys from left frame only
# right - Use keys from right frame only
# outer - Use union of keys
# inner - Use intersection of keys

df1 = pd.merge(names,ages,on='id', how='inner')
df1.set_index('id', inplace=True)

df2 = pd.merge(names,ages,on='id', how='left')
df2.set_index('id', inplace=True)

df3 = pd.merge(names,ages,on='id', how='right')
df3.set_index('id', inplace=True)

df4 = pd.merge(names,ages,on='id', how='outer')
df4.set_index('id', inplace=True)
