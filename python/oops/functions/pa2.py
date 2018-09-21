"""
def changeme(mylist):
	mylist.append([1,2,3,4,5])
	print "inside the function: ",mylist
	return
mylist = [10,20,30,40]
changeme(mylist)
"""
def changeme(mylist):
	mylist = [1,2,3,4]
	print "inside the function",mylist
	return
mylist= [10,20,30,40]
changeme(mylist)	
print "value outside function: ",mylist
