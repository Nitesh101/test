#!/usr/bin/python
def fib(num):
	v1,v2=0,1
	while v2 < num:
		print v2
		v1,v2=v2,v1+v2
	return 

def fib2(num):
	res = [] 
	a,b = 0,1
	while b < num:
		res.append(b)
		a,b=b,a+b
	return res
def fib3(num):
	res = []
	a,b = 0,1
	while b < num:
		res.append(b)
		a,b=b,a+b
	return tuple(res)
