def fac(n):
	if n == 0:
		return 1
	else:
		return n*fac(n-1)
n = input("Enter a value : ")
print fac(n)
