"""
import sys
total_nums = 0
if len(sys.argv) < 2:
		sys.exit('Usage: Error')
else:
	a = int(sys.argv[1])
	b =  int(sys.argv[2])
	print "The result of ",str(a*b)
"""
def fib(n):
	v1,v2=0,1
	while v2 < n:
		print v2,
		v1,v2=v2,v1+v2
	return n 
#fib(10)

def fib2(n):
	res = [] 
	a,b = 0,1
	while b < n:
		res.append(b)
		a,b=b,a+b
	return res
val = fib2(100)
#print val
#print tuple(val)
if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))
