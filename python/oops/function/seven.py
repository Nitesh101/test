def even_num(n):
	val = []
	val2 = []
	for i in n:
		if i % 2 == 0:
			val.append(i)
		else:
			val2.append(i)
	return val,val2
print even_num([1,2,3,4,5,6,7,8,9])
