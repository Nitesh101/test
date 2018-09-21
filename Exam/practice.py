"""
a = raw_input("Enter a string: ")
b = raw_input("Enter word present in given string: ")
if b in a:
	print "b word present in a"
else:	
	print "word not present in string"
a = [1,13,7,5,9]
b = 0
count = 0
for i,j in enumerate(a):
	b+=j
	print i
	if b == 14:
		print i,j,b
		break

a = 'nitesh|warrior|54'
print a.split("|")
"""
list1 = [1,2,3,4]
product = 1
for x in list1:
	product *= x
print x
