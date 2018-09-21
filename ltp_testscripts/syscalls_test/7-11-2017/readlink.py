import os,sys
def readlink():
	''' Return a string representing the path to which the symbolic link points'''
	log = open("file.log","a")
	try:
		src = '/usr/bin/python'
		dst = '/tmp/python'
		os.symlink(src,dst)
		path = os.readlink(dst)
		log.write("readlink    PASS\n")
		log.close()
	except:
		log.write("readlink    FAIL\n")
		log.close()
if __name__=="__main__":	
	readlink()
