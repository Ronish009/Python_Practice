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

"""
1️⃣ axis

axis=0 → concatenate rows (stack one DataFrame on top of the other).

axis=1 → concatenate columns (put DataFrames side by side).



Controls how indexes are aligned. Think of it like SQL joins:
Option	Description
join='outer' (default)	Keep all indexes from both DataFrames. Missing values → NaN.
join='inner'	Keep only indexes present in all DataFrames (intersection).


Parameters of sort_values():
by: Specifies the column to sort by.
ascending: A boolean (True for ascending, False for descending).
inplace: If True, the original DataFrame is modified otherwise a new sorted DataFrame is returned.
na_position: Controls where NaN values are placed. Use 'first' to put NaNs at the top or 'last' (default) to place them at the end.
ignore_index: If True, resets the index after sorting.




"""