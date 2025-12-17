x=4
for i in range(0,x):
    print(i)

se={1,2,34}
print(type(se))
for i in se:
    print(i)

tu=(1,2,3)
print(type(tu))
for i in tu:
    print(i)

s="abc"
print(type(s))
for x in s:
    print(x)

dic=dict({'a':1,'b':2,'c':3})
print(type(dic))
for i in dic:
    print(i, ":", dic[i])


li=[1,2,34]
print(type(li))
for i in li:
    print(i)

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])


s="ronish"
for i in s:
    if i=='r' or i=='o':
        continue
    print(i)


res = [lambda k,x=i:x*k for i in range(1,11)]
k=6
for i in res:
    print(i(k))

'''
k=int(input("Enter the number to find the fictorial"))
res=lambda k:1 if k==0 else k * res(k-1)
print(res(k))
'''

from functools import reduce

fact = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(fact(5))

arr=[1,2,3,45,6]
res = reduce(lambda x,y:x+y,arr)
print(res)

arr=[1,2,3,4,5,6,5,9,65,2,5]
max = reduce(lambda x,y: x if x>y else y, arr)
print(max)
min=reduce(lambda x,y:x if x<y else y, arr)
print(min)

print(sum(range(1,4,2)))
s=["1","2","3","4"]
k=list(map(int,s))
print(k)

k1=list(map(lambda x:int(x),s))
print(k1)


nums = ["123", "2", "3", "4","1","7"]
print("Map")
def string_to_int(s):
    num = 0
    for ch in s:
        num = num*10 +(ord(ch) - ord('0'))
        print(num)
    return num

result = map(string_to_int, nums)
print(list(result))

'''
This is comment
'''
"""
This is comment1
"""

"""
s="ronish"
k=float(s)
print(k)
"""