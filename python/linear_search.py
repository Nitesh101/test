#!/usr/bin/python
lis = [1,2,3,4,5]
print lis
lis2 = input("enter a value you vwant: ")
for val in range(len(lis)):
        if lis[val] == lis2:
                print "found value at index of: ",val
                break
else:
        print "not found"

