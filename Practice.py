x=1
if x==1:
    print("Welcome")
# Dynamically Typed Language
y=10.5
print(type(y))
z=True
print(type(z))
y1=1000000
print(type(y1))
# Functional Programming
a,b=25,24
def f1():
    print("Welcome Ronish: Hello:", a,b)
f1()
from random import *
print(randint(0,9))
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
for i in range(5):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

# Byte Array
x3=[10,20,30]
b=bytearray(x3)
b[0]=50
print(b[0])

# list mmutable
l=[]
print(type(l))
l.append(1);
l.append(2);
l.append(3);
l.append('Ronish')
print(l)
print(l.reverse())
print(l[0])
print(l[1:3])
l1=l*2
print(l1)

#tuple - immutable
l3=(1,2,3,4)
print(l3)
#l3[0]=10;
l4=l3*2
print(l4)

#Range - immutable
r1=range(10)
print(type(r1))
print(r1)
for i in r1: print(i)
print(r1[0])
print(r1[1:3])
#r1[4]=8
#r2=range(10.5,60.8)

#set
print('Set:')
s1={1,2,1,2}
print('Set is',s1)
#print(s1[0])
first_element = next(iter(s1))
print(first_element)
print(list(s1)[1])

#dictionary
print('Dictionary')
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(list(my_dict.keys())[2])
print(type(my_dict))

#Differnce between set and Dictionary
s4={}
s5=set()
s4[100]='RRR'
print(s4)
print(type(s4))
print(type(s5))


#Boolean
print(True+True)
print(True+False)
"""
This is comment
"""
"""
d1=int(input("Enter d1"))
d2=int(input("Enter d2"))
print(d1+d2)

x,y = input("Enter 2").split()
print(x,y)
"""


a2,b2=12,11
a2,b2=b2,a2
print(a2,b2)

s="asdfd"
print(len(s))

"""
s6=9
del s6
print(s6)
"""

#Capital AND, OR AND NOT will not work
b1=True
b2=False
print(b1 and b2)

g=10
print(~g)


#To check the refernce (identity operator)
k1=10
k2=10
k3=20
print(k1 is k2)
print(k1 is not k3)

# Check the value present in the Object (Membership operator)
print("Check Value")
lk1=[1,2,3,4]
search=10
print(search in lk1)
print(search not in lk1)

#Ternary Operator
v1=12
v2=24
min=25 if v1>v2 else 56
print(min)

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)