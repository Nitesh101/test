#!/usr/bin/python
def subset(lis1,lis2):
	for i in lis1:
			if i in lis2:
				print "lis2 is sub set of lis1"
			else:
				print "lis2 is not subset of lis1"
			break
lis1 = input("Enter a list1: ")
lis2 = input("Enter a list2: ")
subset(lis1,lis2)

