import os
log = open("file.log","a")
dirc = os.rmdir("new_folder")
try:
	print os.getcwd()
	os.makedirs("/home/madisnit/Desktop/syscalls_test/new_folder")
	log.write("mkdir PASS\n")
	log.close()
except:
	log.write("mkdir FAIL\n")
	log.close()
