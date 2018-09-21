import os,sys
def unlink():
	''' Remove a file (same as remove(path))'''
	log	= open("file.log","a")
	try:
		os.unlink('new.txt')
		log.write("unlink   PASS\n")
		log.close()
	except:
		log.write("unlink    FAIL\n")
		log.close()
if __name__=="__main__":	
	unlink()
