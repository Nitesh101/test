#!/usr/bin/python
def sum_of(lis1):
	total = 0
	for i in lis1:
		total += i
	return total
lis1 = input("Enter a listof ele: ")
res = []
for val in range(len(lis1)):
	for val1 in range(len(lis1)-1):
		if lis1[val1] > lis1[val1+1]:
			val2 = lis1[val1]*lis1[val1]
			res.append(val2)
			break
print sum_of(lis1)
