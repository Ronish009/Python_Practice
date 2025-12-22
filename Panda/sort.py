from json.decoder import NaN

import pandas as pd
data = {
    "Name": ["Alice", "Eve", "Charlie", "David", "Bob","Ronish"],
    "Age": [28, 22, 25, 22, 28,None],
    "Score": [85, 90, 95, 80, 88,100]
}

df=pd.DataFrame(data)
print(df)

#Sort By Name
print("\n"+"-"*40+"\n")
print(df.sort_values(by='Name'))

print("\n"+"-"*40+"\n")
print(df.sort_values(by='Name', ascending=False))


print(df.sort_values(by='Name', ascending=False, ignore_index=True))
print("\n"+"-"*40+"\n")

print("Example of na_position : ")
print(df.sort_values(by='Age', ignore_index=True, na_position='first'))
print("\n"+"-"*40+"\n")

print("Orignal : \n",df)
print(df.sort_values(by='Age', ignore_index=True, na_position='first', inplace=True))
print("Checking Orignal : \n",df)

print(df.sort_index(ascending=False))

print("Last")
df1=df.sort_values(by='Age', key=lambda x:x.astype('Int64'))
print(df1)