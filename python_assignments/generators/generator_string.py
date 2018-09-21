#!/usr/bin/python

def fun(string):
	length = len(string)
	for ch in string:
		yield ch
	return
res=[]
string=input("Enter a string:")
for char in fun(string):
	res.append(char)
print ''.join(res)	

