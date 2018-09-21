try:
	fh = open("testfile","w")
	fh.write("this is my test fire for except")
except IOError:
	print "Error : can\t find file or read "
else:
	print "witten content in the file"
	fh.close()
