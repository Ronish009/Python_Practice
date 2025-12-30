import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'LA', 'Chicago']}

df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)
# Select row with label 'b'
print(df.loc[['b']])
print(df.loc['b'].iloc[1])

subset = df.loc[['a', 'c']].iloc[:, [0, 2]]
print(subset)

df.loc[df['City'] == 'NY', 'Age'] = 26
print(df)