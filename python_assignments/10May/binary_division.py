#!/usr/bin/python
binvals=raw_input("Enter list of binary valuesin 4 width:")
new_bin=binvals.split(',')
length=len(binvals)

for val in new_bin:
	temp=int(val,2)
	if(temp%5==0):
		print val,','
	


