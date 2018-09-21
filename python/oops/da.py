"""
a = [1, 2, 3, 3, 5, 9, 6, 2, 8, 5, 2, 3, 5, 7, 3, 5, 8]
b = []
[b.append(item) for item in a if item not in b]
print b

val = []
input = raw_input("Enter a string: ")
for i in input:
	val.append(input.upper())
	break
print val

for fizzbuzz in range(50):	
	if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
		print ("fizzbuzz")
		continue
	elif fizzbuzz % 3 == 0:
		print("fizz")
		continue
	elif fizzbuzz % 5 == 0:
		print ("buzz")
		continue
	print(fizzbuzz)
"""
lst = [1,2,3,4,5,6,10]
for index in range(len(lst)-1):
	print index
"""
	for j in range(1,len(lst)):
		if (lst[index]<lst[j]):
"""					
	
	
