#!/usr/bin/python

start=input("enter start in range:")
stop=input("Enter stop in range:")

cnt=0

'''for loop'''

for val in range(start,stop+1,1):
	cnt=0
	for num in range(1,val+1,1):
		if (val%num==0):
			cnt+=1
	if cnt>2:
		print val,"is not prime"
	else :
		print val,"is prime"



'''while loop'''	







