#from collections import Counter
lis = [1,1,2,3,4,2,5,5]
#c = Counter(lis)
#print c
temp = set(lis)
result ={}
for i in lis:
	result[i]=lis.count(i)
print result

