lst1 = ['a','b','a','c','b','a','b','d','c']
lst2 = [1,2,3,4,5,6,7,8,9]
d ={}
for i in range(len(lst1)):
	if (lst1[i]) in d.keys():
		d[lst1[i]].append(lst2[i])
	else:
		d[lst1[i]] = []
		d[lst1[i]].append(lst2[i])
print d
