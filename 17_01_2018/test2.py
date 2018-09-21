lis1 = [3,4,6,2,7,1]
res = []
for val in range(len(lis1)):
	for val1 in range(len(lis1)-1):
		if lis1[val1] > lis1[val1+1]:
			lis1[val1],lis1[val1+1]=lis1[val1+1],lis1[val1]
print lis1
