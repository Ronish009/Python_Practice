"""Panda Practice"""
import pandas
import pandas as pd


#Reading the data from csv file and print
p_read=pd.read_csv('test.csv')
print(p_read.to_string())

print(pd.options.display.max_rows)
print(p_read.head())

df = pd.read_csv('test1.csv')
new_df = df.dropna()
print(new_df.to_string())