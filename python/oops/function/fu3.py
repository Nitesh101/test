def print_value(n):
	l = list()
	for i in range(1,n):
		l.append(i**2)
	print l
n = int(raw_input("Enter a value: "))
print_value(n)
