def count_method(s,lis):
	count = 0
	for i in lis:
		 if i in range(s):
			print s,i,
	return s 
s = input("please enter a number searched: ")
count_method(s,[1,2,3,4,5])
