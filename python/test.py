from collections import defaultdict
lst_1 = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'd', 'c']
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
op = defaultdict(list)
group = zip(lst_1,lst_2)
for i,j in group:
	op[i].append(j)
print op
	
