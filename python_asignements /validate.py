#!/usr/bin/python
paswrd=raw_input("Enter a password:")
upper=0
lower=0
digit=0
spl=0

while True:
#	upper,lower,digit,spl=0,0,0,0
	if (6<=len(paswrd)<=12):
		for ch in paswrd:
			if (ch.isalpha() and ch.isupper()):
				upper+=1
			elif(ch.isalpha() and ch.islower()):
				lower+=1
			elif (ch.isdigit()):
				digit+=1 
			elif ( ch=='$' or ch=='#' or ch=='@'):
				spl+=1
	
		if(upper>=1 and lower>=1 and digit>=1 and spl>=1):
			print "validation succeed" 
		#	print upper,lower,digit,spl
			break	
		else:	
			print "validation Failed"
			paswrd=raw_input("Enter a password:")
	else:
		print ("Validation Failed")
		paswrd=raw_input("Enter a paswrd:")	
