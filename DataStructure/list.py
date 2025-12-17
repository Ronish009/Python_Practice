""" List Example"""
num=[1,2,34,5,6,7,9]
num1=["ronish","raj","gh","fg","jk"]
num3=[1,2,"ronish","kl",8,5.9]
num4=[]
num=[num,num1,num3,num4]
for i in num:
    print(f"List is : {i}  Type is : {type(i)}")

# Indexing of the list
print(num3[2])
#print(num4[0])

# Slicing
print(num3[1:2])
print(num3[:2]) #from start index to 1
print(num4[2:]) #from index 2 to end
print(num3[::2]) #Every second index
print(num3[2:])

# Modification
num5=[1,2,3,4,5,6,7,8,9]
num5[0]=11
print(num5)
num5.append(33)
print(num5)
num5.remove(5)
print(num5)


#Basic Method od List
num6=[1,2,3,4,5,6,7,8,9,10]
num6.append(12)
print("append : ", num6)
num6.insert(0,0)
print("insert : ", num6)
print(f"pop : {num6.pop()} , list  : {num6}")
print(f"Length of List : {len(num6)}")
print(f" 2 is present in List or not :  {2 in num6}")  #Relational Operator

# Concatinating List
n1=[1,2]
n2=[2,4]
n3=n1+n2
print("Concationating List : ",n3)
n1.clear()
print("Clear n1 : ",n1)

#Sort the list
num6=[1,2,3,7,8,9,10,65,4]
print("Orignal List : ",num6)
num6.sort()
print("Sorted List : ",num6)
num6.sort(reverse=True)
print("Sorted Reverse List : ",num6)

#Reverse the List
print("Orignal List : ",num6)
num6.reverse()
print("Reverse List : ",num6)
print("Reverse List : ",num6[::-1])

#Copy the List
num7=num6.copy()
num8=num6
num6.append(100);
print("Copy List : ",num7)
print("Copy List : ",num8)