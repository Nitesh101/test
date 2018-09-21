import os,sys
def popen():
	''' Open a pipe to/from a command returning a file object.'''
	log = open("file.log","a")
	try:
		a = 'mkdir nwdir'
		b = os.popen(a,'r',1)
		log.write("popen   PASS\n")
		log.close()
	except:
		log.write("open    FAIL\n")
		log.close()
if __name__=="__main__":	
	popen()
