mylist = [20,8,7,6,5,4,3,2,1]
for val in range(len(mylist)):
	for val1 in range(len(mylist)-1):
		if mylist[val1] > mylist[val1+1]:
			mylist[val1],mylist[val1+1]=mylist[val1+1],mylist[val1]
print mylist

