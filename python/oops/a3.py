lst = [33,2,4,5,88,7,66]
#print sorted(lst, reverse=True)[1]
#lst.remove(max(lst))
#print max(lst)
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
