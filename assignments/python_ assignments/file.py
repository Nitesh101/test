#!/usr/bin/python

fo = open("employee.txt","r")
data = fo.readlines()
val = raw_input("please enter a value: ")
for line in data:
	if val in line:
		print(''.join(line))
		exit()
else:
	print "not valid record"
fo.close()
