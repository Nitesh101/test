def printinfo(arg1, *vartuple):
	print "output is: "
	print arg1
	for var in vartuple:
		print var
	return
printinfo(10)