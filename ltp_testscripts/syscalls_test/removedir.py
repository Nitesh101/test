import os
log = open("file.log","a")
dirc = os.mkdir("Untitled Folder/")
try:
	os.getcwd()
	os.rmdir("/home/madisnit/Desktop/syscalls_test/Untitled Folder/")
	log.write("rmdir PASS\n")
	log.close()
except:
	log.write("rmdir FAIL\n")
	log.close()	
	
