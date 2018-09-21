#!/usr/bin/python

val=input("Enter a value:")
ele=input("Enter a element to skip:")

for num in val:
	if ele==num:
		continue		
	print num

