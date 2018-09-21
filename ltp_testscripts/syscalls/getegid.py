import os,sys
def getegid():
	''' Return the current process's effective group id.'''
	log = open("file.log","a")
	try:
		os.getegid()
		log.write("getegid    PASS\n")
		log.close()
	except:
		log.write("getegid     FAIL\n")
		log.close()
if __name__=="__main__":
	getegid()
