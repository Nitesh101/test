#summ of all numbers in a list using function
def sum_of(lis):
	sum = 0
	for i in lis:
		sum += i
	return sum
print sum_of([1,2,3,4])
