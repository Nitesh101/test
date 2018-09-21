#!/usr/bin/python

val=input("Enter a list of 5  value:")
ele=input("ENter element to break:")

for num in val:
	if ele==num:
		break
	else:
		print num
