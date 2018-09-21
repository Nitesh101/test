def fib(n):
	if n == 0:
		return 0
	else:
		return fib(n-2) + fib(n-1)
n = input("Enter a  number: ")
print fib(n)
