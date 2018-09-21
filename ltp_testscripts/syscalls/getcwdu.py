import os,sys
def getcwdu():
	'''Return a unicode string representing the current working directory.'''
	log = open("file.log","a")
	try:
		os.chdir("/home/madisnit/Desktop")
		print os.getcwdu()
		log.write("getcwdu    PASS\n")
		log.close()
	except:
		log.write("getcwdu     FAIL\n")
		log.close()
if __name__=="__main__":	
	getcwdu()
