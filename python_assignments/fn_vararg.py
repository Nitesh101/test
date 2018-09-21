#!/usr/bin/python

def fun(*tup):
	res=[]
	cnt=0
	length=len(tup)
	while (cnt<length):
		temp=0
 		for val in tup[cnt]:
			temp=temp+val
		res.append(temp)
		cnt+=1
	return res
tup=(1,2,3,4,5)
tup1=[10,20,30]
res=fun(tup,tup1,tup)
print res
