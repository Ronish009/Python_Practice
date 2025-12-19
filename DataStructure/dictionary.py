"""Dictonary Example"""
dic = {"name":"ronish","age":12,"is_garduated":True,"marks":[95,99,90,92,95],"name":"ronish1"}
#empty dictionary
empty_dic={}

print(type(dic))
print(type(empty_dic))
print(dic)

#Accessing the list
print(dic.get("name"))

#Default value accessing if key is not there
print(dic.get("address"))
print(dic.get("address","galaxy apartment"))


#Modifying value in Dictionary
dic["marks"]=[6,7,8,9]
print(dic)

dic["marks"].append(10)
print(dic)

#Adding key and value in Dictionary
dic["city"]="mumbai"

print(dic)

#deleting the key
del dic["city"]

print(dic.pop("age"))
print(dic)


# checking key is in dictionary
print("name" in dic)
print("name" not in dic)

# length of Dictionary
print(len(dic))
print(dic)

# All key of Dictionary key Method - List
key = dic.keys()
print(key)

# All value of Dictionary values Method - List
value = dic.values()
print(value)

# All items of Dictionary Item Method - Tuple
items = dic.items()
print(items)

# Update to add new Dictionary
dic1={"kkk":"sss"}
dic.update(dic1)
print(dic)

# popitem  used to remove the last key value from dictionary as tuple
tuple3=dic.popitem()
print(tuple3)

# from key is used to create new dictionary with some default value
key4={"a","b","c"}
def_value=1
new_dic=dic.fromkeys(key4,def_value)
print(new_dic)






