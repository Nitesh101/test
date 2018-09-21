#!/usr/bin/python
def fib(n):
	a,b=0,1	
 	for i in range(n):
		a,b=b,a+b
		print a 
	return
num=input("Enter a value:")
fib(num)
