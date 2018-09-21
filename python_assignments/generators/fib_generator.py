#!/usr/bin/python

def fib(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
		yield a
	return	
		
		
num=input("Enter a value:")
fibo=fib(num)
for i in fibo:
	print i
