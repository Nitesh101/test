val = input("Enter a binary number: ")
val2 = []
for i in val:
	b = int(i/2)
	if not (b%5):
		val2.append(i)
print val2 
