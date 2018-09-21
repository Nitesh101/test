#!/usr/bin/python
def bublesort(lis):

#lis = [40,20,50,60,30,10]
#print "Before buble sorting: ",lis
#length=len(lis)
	for index in range(length-1):
		for val in range(length-1-index):
			if lis[val]>lis[val+1]:	
				temp=lis[val]
				lis[val]=lis[val+1]
				lis[val+1]=temp
lis = [40,20,50,60,30,10]
print "Before buble sorting: ",lis
length = len(lis)
bublesort(lis)
print lis
			
