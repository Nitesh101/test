import os,sys
def statvfs():
	''' Perform a statvfs system call on the given path'''
	log = open("file.log","a")
	try:
		statinfo = os.statvfs("popen.py")
		log.write("statvfs   PASS\n")
		log.close()
	except:
		log.write("statvfs    FAIL\n")
		log.close()
if __name__=="__main__":	
	statvfs()
