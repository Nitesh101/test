val=raw_input("Enter a value: ")
val2=val.split(",")
val3=tuple(val2)
print val2
print val3

lis=[]
val = input("Eneter a values: ")
for i in range(val):
	if (i%4) and (i%5!=0):
		lis.append(str(i))
print ','.join(lis)

d={}
val = input("Enter a number: ")
for i in range(val+1):
	d[i]=i*i
print d

l1=[2, 13, 5, 7, 6, 9]
for i in l1:
	for j in l1:
		if i+j == 15:
			print "The indexex of: ",l1.index(i),i
lis = []
for i in range(1000, 3001):
	if (i%2==0):
		lis.append(str(i))
print ','.join(lis)
