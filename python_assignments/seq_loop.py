#!/usr/bin/python

val=[11,12,13,14,15]
res=[]
for num in range(10,100,10):
#	print range(num)
	res=res+val
	val[0]= val[0]+10
	val[1]=val[1]+10
	val[2]=val[2]+10
	val[3]=val[3]+10
	val[4]=val[4]+10

print res	
