#!/usr/bin/python
def binary_search(lis,item):
	low=0
	up=len(lis)
	while (low<=up):
		mid=(low+up)/2
		if(item<lis[mid]):
			up=mid-1
		elif(item>lis[mid]):
			low=mid+1
		else:
			return mid
	return "NONE"
lis=[3,2,4,53,8,2,9]
print lis
lis=sorted(lis)
item=input("enter item to be serached in binary: ")
index = binary_search(lis,item)
if index == "NONE":
	print "item not found"
else:
	print "item found at",index
