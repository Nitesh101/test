#!/usr/bin/python
x=input("Enter X:")
y=input("ENter Y:")
list1=[]

for i in range(x):
	temp=[]
	for j in range(y):
		temp.append(i*j)
	list1.append(temp)
print list1		
	
