lst = [1,2,3,4,2,4,5,6]
op=[]
for x in lst:
	if lst.count(x)==1:
		op.append(x)
print op
