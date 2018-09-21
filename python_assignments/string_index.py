#!/usr/bin/python
def fun(str1,str2):
	if str2 in str1 :
		print str2,"is in ",str1
		print 'index is ',str1.index(str2)
		print 'count is ',str1.count(str2)
	else:
		print str2," is not in ",str1
		
	return

str1=input("Enter string 1:")
str2=input("Enter string 2:")
fun(str1,str2)

