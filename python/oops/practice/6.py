#from collections import Counter
lis = [1,1,2,2,3,2,1,3,4]
"""
#c = Counter(lis)
#print c
temp = set(lis)
result = {}
for i in temp:
	result[i]=lis.count(i)
print result
"""
temp = set(lis)
result = {}
for i in lis:
	result[i]=lis.count(i)
print result
