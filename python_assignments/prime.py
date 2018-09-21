#!/usr/bin/python
import math
val1=input("enter an integer:")
cnt=0

'''for loop'''

for num in range(1,val1+1,1):
	if (val1%num==0):
		cnt+=1
		
if cnt>2:
	print val1,"is not prime"
	
else :
	print val1,"is prime"



'''while loop'''	
val=input("Enter a number:")
num=1
cnt=0
while (num<=val+1):
	if(val%num==0):
		cnt+=1
	num+=1
if cnt>2:
	print val,"is not prime"
else:
	print val,"is prime"



