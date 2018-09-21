#!/usr/bin/python
def asen(num):
	if num > 0 :
		asen(num-1)		
		print num,
	return

def decen(num):
	if num > 0 :	
		print num,
		decen(num-1)		
	return
num = input("Enter Number : ")
print "Number in ascending order :",
asen(num)
print
print "Number in descending order :",
decen(num)
