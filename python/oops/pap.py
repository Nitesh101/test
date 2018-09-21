lst = [22,3,4,44,55,67,8,89]
print sorted(lst, reverse=True)[5]


"""
if lst[0] > lst[1]:
	l,m = lst[0],lst[1]
else:
	l,m=lst[1],lst[0]
for x in lst:
	if x>m:
		if x>l:
			m,l=l,x
		else:
			m = x
print m
"""
