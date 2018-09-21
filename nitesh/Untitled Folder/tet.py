val = [2,3,4,8,1,10]
for i in range(0,len(val)):
	for j in range(i+1,len(val)):
		if val[i]>val[j]:
			break
	print val[i]

