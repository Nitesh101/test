#!/usr/bin/python

def fun(val):
	
	for num in range(val):
		yield num

val= input("Enter a range value:")
for temp in fun(val):
	print temp
