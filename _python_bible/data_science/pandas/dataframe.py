import pandas as pd

data = {'Name': ['Anna', 'Bob', 'Charles','Daniel', 'Evan', 'Fiona','Gerald', 'Henry', 'India'],
        'Age': [24,32,35,45,22,54,55,43,25],
        'Height': [176,187,175,182,176,189,165,187,167]}


df = pd.DataFrame(data)

print(df['Name'][1])
print(df[['Name', 'Height']])

## Basic Functions
# df.T - Transpose
# df.dtype - Data type of each column
# df.ndim - Number of dimensions
# df.shape - Shape of the dataframe
# df.size - Number of elements
# df.head(n) - First n rows
# df.tail(n) - Last n rows

## Statistical Functions
# count() - Number of non-null values
# sum() - Sum of values
# mean() - Mean of values
# median() - Median of values
# mode() - Mode of values
# std() - Standard deviation of values
# min() - Minimum value
# max() - Maximum value
# abs() - Absolute value
# prod() - Product of values
# describe() - Summary statistics

print(df['Age'].mean())
print(df['Height'].median())
print(df.mean())

## Apply np Function
import numpy as np
print(df['Age'].apply(np.sin))

## Lambda Function
print(df['Age'].apply(lambda x: x**100))
df = df[['Age', 'Height']]
print(df.apply(lambda x: x.max() - x.min()))

