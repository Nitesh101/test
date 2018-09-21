fo = open("test.txt","rw+")
print "Name of the file:", fo.name
line = fo.readline()
print "Read Line: %s"%(line)
line = fo.readline(5)
print "Read Line: %s"%(line)
fo.close()
