x = input("Enter a input of x: ")
y = input("Enter a input of y: ")
lis = []
for i in range(int(x)):
	temp = []
	for j in range(int(y)):
		temp.append(i*j)
	lis.append(temp)
print lis 
