val = raw_input("Enter a input : ")
val2 = val.split()
remove = set(val2)
val3 = sorted(remove)
for i in val3:
	print i,
