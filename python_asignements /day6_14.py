def multiply():
	val = input("Enter Start Number: ")
	val2 = input("Enter End Number: ")
	for i in range(val,val2):
		if (i*7) == 0:
			yield i
for index in multiply():
	print index
