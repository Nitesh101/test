#!usr/bin/python
import os
import time
import sys

def prime():
	num = 407
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				print(num,"is not a prime number")
           			print(i,"times",num//i,"is",num)
           			break
		else:
			print(num,"is a prime number")      
	else:
   		print(num,"is not a prime number")

def fib():
	nterms = 10
	n1 = 0
	n2 = 1
	count = 2
	if nterms <= 0:
   		print("Please enter a positive integer")
	elif nterms == 1:
  		print("Fibonacci sequence upto",nterms,":")
   		print(n1)
	else:
   		print("Fibonacci sequence upto",nterms,":")
   		print(n1,",",n2)
   	while count < nterms:
       		nth = n1 + n2
		print(nth),
       		n1 = n2
       		n2 = nth
       		count += 1	

def fact():
	def print_factors(x):
		print("The factors of",x,"are:")
   		for i in range(1, x + 1):
       			if x % i == 0:
           			print(i)

	num = 320
	print_factors(num)
	
processid = os.fork()
if(processid>0):
	processid=os.fork()
	print "parent1"
	if (processid>0):
		print "parent2"
		processid =os.fork()
		if (processid>0):
			print "parent3"	
		elif (processid==0):
			prime()
	elif(processid==0):
	#processid = os.fork()
	#if (processid==0):
		fib()
elif(processid==0):
	#processid=os.fork()
	#if(processid ==0):
	fact()
else:
	print "program is comleted thank you"
 
sys.exit(0)

