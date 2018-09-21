val = [2,33,4,54,2,1]
if val[0] > val[1]:
	l,m = val[0],val[1]
else:
	l,m = val[1],val[0]
for x in val:
	if x > m:
		if x > l:
			m,l=l,x
		else:
			m = x
print m
