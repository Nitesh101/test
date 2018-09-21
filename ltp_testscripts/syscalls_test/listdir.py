import os
log = open("file.log","a")
try:
	os.listdir("/home/madisnit/Desktop")
	log.write("listdir PASS\n")
	log.close()
except:
	log.write("listdir FAIL\n")
	log.close()
