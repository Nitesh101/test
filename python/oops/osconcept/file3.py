fo = open("test.txt","rw+")
print "Name of the file : ",fo.name
for index in range(5):
	line = fo.next()
	print "Line No %d - %s"%(index,line)
fo.close()
