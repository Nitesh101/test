#!/usr/bin/python

val1 = input("Enter a list1: ")
val2 = input("Enter a list2: ")
res = list(set(val1)&set(val2))
print res


lis1 = range(1,10,1)
lis2 = range(1,20,2)
print list(set(lis1)&set(lis2))

lis1 = range(10,1,-1)
lis2 = range(1,20,2)
print list(set(lis1)&set(lis2))

lis1 = range(10,1,-1)
lis2 = range(20,1,-2)
print list(set(lis1)&set(lis2))

"""
lst1 = [1,2,3,4,5,6]
lst2 = [5,4,10,20,2]
op  = []
for i in lst1:
	if i in lst2:
		op.append(i)
print op
"""
