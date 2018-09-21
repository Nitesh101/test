fo = open("test.txt","wb")
print "Name of the file: ",fo.name
fid = fo.fileno()
print fid
fo.close()
