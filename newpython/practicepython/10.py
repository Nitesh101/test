list1 = [1,13,5,9]
for i in range(0,len(list1)):
	for j in range(1,len(list1)):
		if list1[i]+list1[j] == 14:
			print i,j
			print list1[i],list1[j],
			print "is Equal to: ",list1[i]+list1[j]

			
		break

