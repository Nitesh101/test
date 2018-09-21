#!/usr/bin/python
lis = [2,7,3,9,1,6,8]
print lis
lis = sorted(lis)
print lis
item=input("enter item to be searched: ")
def binary_search(lis,item):
        low = 0
        up = len(lis)
        while(low<=up):
                mid=(low+up)/2
                if (item<lis[mid]):
                        up=mid-1
                elif (item>lis[mid]):
                        low=mid+1
                else:
                        return mid
        return "NONE"
index = binary_search(lis,item)
#print index
if index == "NONE":
        print "item not found"
else:
        print "item found at",index

