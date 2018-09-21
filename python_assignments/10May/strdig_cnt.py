#!/usr/bin/python


string=input("Enter a string:")

num_cnt=0
ltr_cnt=0
'''
for ch in string:
	if (ord(ch)<=57 and ord(ch)>=48):
		num_cnt+=1
	elif ((ord(ch)<=90 and ord(ch)>=65) or (ord(ch)>=97 and ord(ch)<=122)):
		ltr_cnt+=1
'''

for ch in string:
	if ch.isalpha() == True:
	 	ltr_cnt+=1
	elif ch.isdigit()==True:
		num_cnt+=1

print "Numbers:",num_cnt
print "Letter:",ltr_cnt
