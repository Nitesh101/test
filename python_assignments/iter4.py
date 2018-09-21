#!/usr/bin/python
from itertools import permutations
from itertools import combinations
string=input("Enter a string:")
itr=iter(string)
res=[]
while True:
	try:
		res.append(itr.next())
	except StopIteration:
		break

#res=sorted(res)
cnt=0
while cnt<=len(string):
	for num in permutations(res,cnt):
		print ''.join(num)
			
	cnt+=1

	
