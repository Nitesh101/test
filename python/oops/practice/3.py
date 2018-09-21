def string(lis):
	x =[]
	for i in lis:
		if i not in lis:
			x.append(i)
	return x
print (string([1,2,2,3,4,4]))	
