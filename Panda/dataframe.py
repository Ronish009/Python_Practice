"""Data Frame Examples"""

import pandas as pd


def customPrint():
    """Heading"""
    print("\n" + "-" * 40)


def println(name=""):
    """Custom print"""
    print("\n" + name + ":" + "\n")


#Create Dataframe using list
customPrint()
print("Create DataFrame using list ")
number = [12, 13, 45, 67, 78]
println("List")
print(number,"\n")
print("DataFrame : \n")
print(pd.DataFrame(number, columns=['Age'], index=['a', 'b', 'c', 'd', 'e']))

customPrint()

#Create Dataframe using Dictionary
dic={'Name':['Ronish','Raj','Rohit'],'Age':[33,34,56]}
println("Create Dataframe using Dictionary ")
println("Dictionary")
print(dic,"\n")
print("DataFrame : \n")
print(pd.DataFrame(dic))

customPrint()

#Working With Rows and Columns in Pandas DataFrame
println("Working With Rows and Columns in Pandas DataFrame")
data = {'Name':['Jai', 'Prince', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
println("Dictionary")
print(data,"\n")
println("DataFrame")
print(pd.DataFrame(data),"\n")
#Column Selection
println("Column Selection")
df=pd.DataFrame(data)
print(df[['Name']])
#Row Selection
println("Row Selection")
df1=pd.DataFrame(data,columns=['Age','Name','Address'])

print(df1.iloc[[1]],"\n")
print(df1.iloc[[1,2]],"\n")

#df2=df1.set_index('Name')
df_row=pd.DataFrame(data)
print(df_row.query("Name=='Jai'"))
print()
df_row_index=df_row.set_index('Name')
print(df_row_index.loc[['Jai']],"\n")
print()
print(df[df['Name']=='Jai'],"\n")
print()

df_row_index1=df.set_index('Age')
print(df_row_index1.loc[[22]],"\n")
print(df_row_index1.loc[22],"\n")
rows=df_row_index1.loc[22]
print(rows['Name'],"\n")
print(rows.iloc[0],rows.iloc[1],rows.iloc[2])
print(rows['Name'],rows['Qualification'],rows['Address'])


customPrint()

dataf = pd.DataFrame({
    'Name': ['Jai', 'Prince', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32]
})

#print(dataf.loc[['Name']],"\n")
print(dataf[['Name']], "\n")  # Jai
print(dataf.loc[[0, 2], ['Name', 'Age']], "\n")


data56 = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}
df=pd.DataFrame(data56)

df56 = df[df['Name']=='John']
print(df56)






print("Ronish")
print(df56.loc['John'])
print(df56.loc[['John','Alice']])
print(df56['Name'].iloc[2])
#print(df56.loc['Name'])
print(df56.loc[['Alice']])
print(df56.loc['Alice'][0])
print("Ronish1")
print(df56.iloc[1][0])
print("Ronish2")
print(df56.iloc[1,0])

non_null_rows1 = df.loc[df['Name'].notnull(),'Age']
print("\nRows where column 'B' is not null:")
print(non_null_rows1[0])


non_null_rows = df.loc[df['Name'].notnull()]
print("\nRows where column 'B' is not null:")
print(non_null_rows)
print(data56['Age'])