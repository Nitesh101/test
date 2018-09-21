import os,sys
def major():
	'''Extracts a device major number from a raw device number'''
	log = open("file.log","a")
	try:
		path = "/home/madisnit/Desktop/file.py"
		info = os.lstat(path)
		major_dnum=os.major(info.st_dev)
		log.write("major    PASS\n")
		log.close()
	except:
		log.write("major    FAIL\n")
		log.close()
if __name__=="__main__":	
	major()
