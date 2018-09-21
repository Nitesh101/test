"""
"Required arguments""
def printme(str):	
	print str
	return
printme('nitesh')
"keyword arguments"

def printme(str):
	print str
	return
printme(str='name')
"""
#Default arguments
def printinfo(name,age=35):
	print 'Name',name
	print 'Age',age
	return
printinfo(name='tesh',age=20)
printinfo(name='satheesh')
