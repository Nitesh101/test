lst_1 = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'd', 'c']
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = {}
for i in lst_1:
	for j in lst_2:
		if i not in d.items():
			d.append(i)
		else:
			d.append(j)
print d
		
