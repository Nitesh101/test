#!/usr/bin/python
values_in = raw_input("Enter a binary value: ")
numbers = values_in.split(',')
op =[]
for val in numbers:
	if int(val,2)%3==0:
		op.append(val)
print tuple(op)

