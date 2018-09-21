list1 = [1,20,3,2,30]
res = []
while list1:
	minium = list1[0]
	for i in list1:
		if i < minium:	
			minium = i
	res.append(minium)
	list1.remove(minium)
print res
