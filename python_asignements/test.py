"""
def fib(n):
	res=[]
	a,b=0,1
	while b < n:
		res.append(b)
		a,b=b,a+b
	return res
v = fib(100)
print v
"""
lst = [-5, 7, -3, 4, -9, 10, -1, 11]
op = []
index = 0
for val in lst:
	if val > 0:
		op.insert(index,val)
	else:
		op.append(val)
print op
