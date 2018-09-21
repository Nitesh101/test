#!/usr/bin/python
"""
#ifdef PROGRAM1
#normal method
lis = [1,2,3,4,5]
print lis
lis2 = input("enter a value you vwant: ")
for val in range(len(lis)):
	if lis[val] == lis2:
		print "found value at index of: ",val
		break
else:
	print "not found"
#endif
"""
#ifdef PROGRAM2
#using functions
def linear_search(obj,item):
	for val in range(len(obj)):
		if obj[val] == item:
			return val
	return -1
obj = [1,2,3,4,5,6]
print obj
item = input("enter a value of index in linear: ")
print "item found at : ",linear_search(obj,item)
#endif

