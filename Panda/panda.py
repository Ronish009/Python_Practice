"""Panda Practice"""
import pandas as pd

print("\n"+"-"*40+"\n")
print("Data Frame with default index:")
print()
#To demonstrate the dataset as Frame (Column and Rows)
dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'rating': [3, 7, 2]
}
my_var=pd.DataFrame(dataset)
print(my_var)


#To demonstrate the dataset as Frame with specific index
print("\n"+"-"*40+"\n")
print("Data Frame with specific index:")
print()
my_var=pd.DataFrame(dataset,index=['a','b','c'])
print(my_var)

print("\n" + "-"*40 + "\n")

#Series from a list
print("\n"+"-"*40+"\n")
print("Data Frame with specific index:")
a=[1,0,9,8]
my_ser=pd.Series(a, index=["a","b","c","d"])
print(my_ser.to_string())