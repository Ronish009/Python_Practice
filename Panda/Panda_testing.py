from json.decoder import NaN

import pandas as pd
from IPython.core.display_functions import display

lst = ['Geeks', 'For', 'Geeks', 'is',
            'portal', 'for', 'Geeks']

df=pd.DataFrame(lst, columns=['XYZ'])
print(df)
display(df)

data = {'Name':['Tom', 'nick', 'krish', 'jack','Ronish'],
        'Age':[30, None, None, 55,60]}


df1=pd.DataFrame(data)

print("testing1\n")
columns = list(df1)
print(columns)
for i in columns:
    print(df1[i][2])
df1['Age_extended']=df1['Age'].interpolate();
print(df1)
print("====isnull===")

data3 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df3=pd.DataFrame(data3, index=['x','y','c','d'],columns=['Name','Age'])
print(df3)
print(df3[['Name','Age']].head(2))
print(type(df3[['Name','Age']]))
print(type(df3['Name']))
print(df3[['Name']].to_string().upper())
print(df3['Name'].str.upper())

print("==========")
print(df3)
print("======R====")
first=df3.loc[['x','d']] #Index label
print(first)

first=df3.loc[['x']]['Name'] #Index label
print(first)

first1=df3.iloc[[0,1]] #Index position
print(first1)

print("============CSV================")
data5=pd.read_csv("panda_testing.csv", index_col=['Name'])

print(type(data5))
print(data5)
print("============CSV1================")
print(data5[data5['Qualification']=='MA'])
#result = data5.xs(24, level='Age') work when colum used as index
#print(result)
#print(type(result))
print("============CSV2================")
first5 = data5["Age"]

print(first5)