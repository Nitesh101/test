val = input("Enter a input: ")
l = len(val)
if l%2 == 0:
	list1 =[]
	for i in range(1,l,2):
		v=val[i-1]+val[i]
		list1.append(v)
	print list1
	t=[]
	for i in range(2,len(list1),1):
		sumn=int(list1[i-2])+int(list1[i-1])
		if sumn is int(list1[i]):
			t.append(sumn)
	print t
			
else:
	print "no"
