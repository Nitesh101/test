lst = [22,33,45,6,7,47,88]
if lst[0] > lst[1]:
	l,m = lst[0],lst[1]
else:
	l,m = lst[1],lst[0]
for x in lst:
	if x > m:
		if x > l:
			m,l=l,x
		else:
			m = x
print m
