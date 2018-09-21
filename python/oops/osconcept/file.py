fo = open("test.txt","wb")
print "Name of the file : ",fo.name
ret=fo.isatty()
print ret
fo.close()
