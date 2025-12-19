"""Set Functionality"""
set1={1,2,3,4,6,7,8}
print(set1)


#add
set1.add(10)
print(set1)

#update
set2={11,12}
set1.update(set2)
print(set1)

#remove
set1.remove(12)
print(set1)

#discard it will check whether it is present or not, if not discard it, if present remove it
set1.discard(12)
print(set1)
set1.remove(11)
print(set1)

#pop it remove the random index and return the value
print(set1.pop())

#clear clear the set

s1={1,2,3}
s2={2,3}

#union
s3=s1.union(s2)
print(s3)

#intersection
s4=s1.intersection(s2)
print(s4)

#subset
s5=s1.issubset(s2)
print(s5)

#superset
s6=s1.issuperset(s2)
print(s6)

#symetricdiffernece
s7=s1.symmetric_difference(s2)
print(s7)


