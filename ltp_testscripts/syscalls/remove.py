import os,sys
log = open("file.log","a")
try:
	os.listdir(os.getcwd())
	os.remove("new.txt")
	print os.listdir(os.getcwd())
	log.write("remove   PASS\n")
	log.close()
except:
	log.write("remove FAIL\n")
	log.close()
