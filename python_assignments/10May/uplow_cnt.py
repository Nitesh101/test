#!/usr/bin/python
string=input("Enter a string:")
up_cnt=0
lw_cnt=0
for ch in string:
	if ord(ch)<=90 and ord(ch)>=65:
		up_cnt+=1
	elif ord(ch)<=122 and ord(ch)>=97:
		lw_cnt+=1	

print "Upper case:",up_cnt
print "Lower case:",lw_cnt		
