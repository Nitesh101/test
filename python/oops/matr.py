x  = raw_input("enter a value: ")
y = raw_input("enter a va;ue: ")
list1 = []
for i in range(len(x)):
	temp =[]
	for j in range(len(y)):
		temp.append(i*j)
	list1.append(temp)
print list1	
