#!/usr/bin/python
list1=[1,2,3,4]
for index in range(0,len(list1)):
	if list1[index]<list1[index+1]:
		print list1[index]
	else:
		print list1[index+1]
