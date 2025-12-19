"""Function Practice"""
number_input=input("Enter a number separted with space : ")
numbers=[int(x) for x in number_input.split(" ")]
print(numbers)

print("Max Value : ",max(numbers),end='')
print(" Min Value : ",min(numbers))


#Calling Function
def greet(name):
    print(name)

greet(name="ronish")

#Remove duplicate element without using built function
a=[1,2,3,1,2,3,1,2,3]
b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)





