#!/usr/bin/python
def strcmp(str1,str2):
	if (str1==str2):
		print 0,"Equal"
	elif (str1<str2):
		print -1,"str1 less than str2 "
	else:
		print 1, "str1 greater than str2"
	return


str1=input("Enter string 1:")
str2=input('Enter string 2:')

strcmp(str1,str2)

