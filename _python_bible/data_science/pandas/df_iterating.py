import pandas as pd

data = {'Name': ['Anna', 'Bob', 'Charles','Daniel', 'Evan', 'Fiona','Gerald', 'Henry', 'India'],
        'Age': [24,32,35,45,22,54,55,43,25],
        'Height': [176,187,175,182,176,189,165,187,167]}


df = pd.DataFrame(data)

## Iterating
for x in df['Age']:
    print(x)

## Staticstical Functions
# iteritems() - Iterates over each column as key, value pair
# iterrows() - Iterates over each row as key, value pair
# itertuples() - Iterates over each row as named tuple

for key, value in df.iteritems():
    print("{}: {}", key, value)

for index, value in df.iterrows():
    print("{}: {}", index, value)