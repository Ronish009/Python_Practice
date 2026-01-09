#Lamda Expression
from functools import reduce

s1='ronish'
s2 = lambda x:x.upper()
print(s2(s1))

#Finding
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))

#Odd and Even
s = lambda x:"Even" if x%2==0 else "Odd"
print(s(3))

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

cal = lambda x,y:(x+y,x-y)
print(cal(3,4))


n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))


a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)


def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

li = [x for x in range(1, 5) if x%2==0]
for i in li:
    print(i)