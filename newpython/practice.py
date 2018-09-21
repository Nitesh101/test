"""
val = input("enter a value: ")
ele = input("enter break value: ")
for i in val:
	if ele == i:
		break
	else:
		print i

count = 0
while True:
	val = raw_input("enter a string: ")
	if val == "quit":
		print count
		break
	else:
		count+=1
		continue
"""
list1 = input("enter a list: ")
list2 = []
for i in list1:
	if i not in list2:
		list2.append(i)
print list2

"""
list1 = input("enter a list: ")
val = set(sorted(list1))
print val
"""








