import pandas as pd
data = pd.read_csv("test25.csv")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(data)
print(data['emp_name'])