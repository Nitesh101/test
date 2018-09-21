#!/usr/bin/python

string=raw_input("Enter Transaction details:")

res=0
while True:
	if (string[0]=='D'):
		temp=int(string[1:])
		res=res+temp
		string=raw_input("Enter Transaction Details:")
	elif(string[0]=='W'):
		temp1=int(string[1:])
		if(res>=temp1):
			res=res-temp1
		else:
			print "Low Balance"
		string=raw_input("Enter Transaction Details:")
	elif(string=='quit'):
		break
	else:
		print ("Enter properly with D or W")
		string=raw_input("Enter Transaction Details:")
		
print "Total is",res
