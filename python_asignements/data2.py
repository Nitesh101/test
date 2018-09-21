list1 = ['abc','xyz','aba','1221']
ctr = 0
for i in list1:
	if len(i) > 1 and i[0] == i[-1]:
		ctr += 1
print ctr	
