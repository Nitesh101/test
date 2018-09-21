"""
lis = [(1,2),(3,4),(5,6)]
lis2 = []
for i in lis:
	lis3=[]
	for index in range(len(lis)-1,-1,-1):
		lis3.append(lis[index])
	tup = tuple(lis3)
	lis2.append(tup)
print lis2

a = [(1,2),(3,4),(5,6)]
res1 = []
for val in a:	
	res = []
	for index in range(len(val)-1,-1,-1):
		res.append(val[index]
	tup = tuple(res)
	res1.append(tup)
print res1

lis = [1,2,3,4,5,6]
res1 = []
for val in lis:
	res = []
	for i in range(len(lis)-1,-1,-1):
		res.append(lis[i])
	lis2 = list(res)
	res1.append(lis2)
print res1

total = {}
def insert(items):
	if items in total:
		total[items] += 1
	else:
		total[items] = 1
insert("Apple")
insert("Ball")
insert("Apple")
print len(total)

a= {}
a[1] = 1
print a
a['1'] =2
print a
a[1]= a[1]+1
print a
count = 0
for i in a:
	count += a[i]
print count

numbers = {}
letters = {}
comb = {}
numbers[1] =56
numbers[3] = 7
letters[4] = 'B'
comb['Numbers'] = numbers
comb['Letters'] = letters
print comb

a = {}
a[2] = 1
a[1] = [2,3,4]
print a[1][1]

a={'B':5,'A':9,'c':7}
print sorted(a.items())
"""
from collections import defaultdict
lst = ['a','b','a','c','b','a','b','d','c']
lst2 = [1,2,3,4,5,6,7,8,9]
op = defaultdict(list)
group = zip(lst,lst2)
for i,j in group:
	op[i].append(j)
print op
"""

