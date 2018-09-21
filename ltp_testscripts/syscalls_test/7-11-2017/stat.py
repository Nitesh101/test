import os,sys
def stat():
	''' Perform a stat system call on the given path.'''
	log = open("file.log","a")
	try:
		statinfo = os.stat("popen.py")
		log.write("stat   PASS\n")
		log.close()
	except:
		log.write("stat    FAIL\n")
		log.close()
if __name__=="__main__":	
	stat()
