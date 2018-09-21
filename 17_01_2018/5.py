#!/usr/bin/python

def meargeList(list1, list2):
	list3 = []
	count = len(list2)
	for index in range(len(list1)):
		list3.append(list1[index])
		print "len",len(list2)
		if len(list2) != 0:
			list3.append(list2[0])
			list2.remove(list2[0])
	return list3

list1 = [5, 7, 17, 13, 11]
list2 = [12, 10, 2, 4, 6]
print list1
print list2
list1 = meargeList(list1, list2)
print "list1 ", 
for val in list1:
	print "->", val ,
print "\nlist2: ", list2

print "\n\n input 2\n "
list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8]
print list1
print list2
list1 = meargeList(list1, list2)
print "list1 ", 
for val in list1:
	print "->", val ,
print "\nlist2: ", list2
