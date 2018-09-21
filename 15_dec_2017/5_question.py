#!/usr/bin/python
val = input("Enter a value: ")
dict = {}
for index in range(2,val):
	dict[index] = index*index
print dict
