res = 0
lis1 = []
num = input("Enter number ele: ")
for i in range(num):
	val = input("Enter a element: ")
	lis1.append(val)
print lis1
for index in lis1:
	if index <= 0:
		min1 = min(lis1)
		lis1.remove(min1)
		min2 = min(lis1)
		lis1.remove(min2)
		res += min1 * min2
	else:
		max1 = max(lis1)
		lis1.remove(max1)
		max2 = max(lis1)
		lis1.remove(max2)
		res += max1 * max2
if len(lis1) == 1
	res += lis1[0]
print "max sum of ele = ",res
