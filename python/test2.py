lst_1 = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'd', 'c']
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
d = {}
for i in range(len(lst_1)):
	if lst_1[i] in d.keys():
		d[lst_1[i]].append(lst_2[i])
	else:
		d[lst_1[i]]=[]
		d[lst_1[i]].append(lst_2[i])
print d
"""
d = {}
for i in range(len(lst_1)):
	if lst_1[i] in d.keys():
		d[lst_1[i]].append(lst_2[i])
	else:
		d[lst_1[i]]=[]
		d[lst_1[i]].append(lst_2[i])
print d
