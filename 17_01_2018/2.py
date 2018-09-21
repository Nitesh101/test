#!/usr/bin/python
#list1 = [-1, 9, 4, 5, -4, -7, 0]
res = 0
list1 = []
num = input("enter num of ele: ")
for rng in range(num):
	val = input("enter element: ")
	list1.append(val)
print list1
for index in list1:
	if index <= 0:
		min1 = min(list1)
		list1.remove(min1)
		min2 = min(list1)
		list1.remove(min2)
#		print min1, min2
		res += min1 * min2
		
	else:
		max1 = max(list1)
		list1.remove(max1)
		max2 = max(list1)
		list1.remove(max2)
#		print max1, max2
		res += max1 * max2

if len(list1) == 1:
		res += list1[0]
print "max sum of elements = ", res

