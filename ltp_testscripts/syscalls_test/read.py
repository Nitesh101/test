import os
log = open("file.log","a")
try:
	f = open("file2.txt","r")
	f.read()
	log.write("read PASS\n")
	log.close()
	f.close()
except:
	log.write("read FAIL\n")
	log.close()
