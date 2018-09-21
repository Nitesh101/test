a = [1,2,3,2,3,2,1,4,5,33,2,3,33]
b = []
for i in a:
	if i not in b:
		b.append(i)
print b
