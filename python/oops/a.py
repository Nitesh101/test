lis = ['x','x','a','b','x']
temp =set(lis)
result = {}
for i in lis:
	result[i] = lis.count(i)
print result
