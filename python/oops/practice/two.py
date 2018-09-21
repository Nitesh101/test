"""
def revserse(val):
	str = " "
	if val>0:
		str = val[::-1]
	return str
print revserse('123abcd')

def max_of_two(x,y):
	if x > y:
		return x
	return y

def sum_of(lis):
	total = 0
	for x in lis:
		total += x
	return total
print sum_of([3,4,5,6])

def mul(number):
	total = 1
	for x in number:
		total *= x
	return total
print mul([3,4,5])

def sum(number):
	total = 1
	for i in number:
		total += i
	return total
print sum([2,3,4])

def reverse(lis):
	str = " "
	if lis > 0:
		str = lis[::-1]
	return str
print reverse('123abc')

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
#n = raw_input("Enter a input: ")
print(factorial(4))
"""
def string(s):
	d={"uppercase":0,"lowercase":0}
	for i in s:
		if i.isupper():
			d['uppercase'] += 1
		elif i.islower():
			d['lowercase'] += 1
		else:
			pass
	print ("No of upper case",d['uppercase'])
	print ("No of lower case",d['lowercase'])
string("THIS IA a nitesh")
