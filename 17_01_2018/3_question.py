#!/usr/bin/python
def fib(n):
	a,b = 0,1
	for i in range(2,n):
		if n %i == 0:
			print "Number",n,"is not fibonacci-prime"
			break
		for i in range(n+1):
			a,b=b,a+b
			break
	else:
			print "Number",n,"is fibanacci-prime"
	return
		
n = input("Enter a value: ")
fib(n)
		
