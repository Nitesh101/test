def fib(n):
	v1,v2=0,1
	while v2 < n:
		print v2,
		v1,v2=v2,v1+v2
	return n 
fib(10)
