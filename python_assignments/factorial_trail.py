#!/usr/bin/python


val=input("Enter zero count:")
num=1
fact=1
while(num<10):
	fact=fact*num
	num=num+1
	string =str(fact)
	length= len(string)-1

	if (string[length:length-val])=='0'*val:
		print "num is",num
		break

	
