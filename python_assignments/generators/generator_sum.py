#!/usr/bin/python

def fun(list1):
	for val in list1:
		yield val
	return


list1=input("Enter a list:")
res=0
for index in fun(list1):
	res=res+ index

print res
