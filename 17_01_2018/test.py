lis1 = [-1,0,1]
res = 0
for i in lis1:
	if i <= 0:
		min1 = min(lis1)
		lis1.remove(min1)
		min2 = min(lis1)
		lis1.remove(min2)
		res += min1 * min2
if len(lis1) == 1:
	res += lis1[0]
print res
