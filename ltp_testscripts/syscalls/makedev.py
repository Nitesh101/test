import os,sys
def makedev():
	'''Composes a raw device number from the major and minor device numbers'''
	log = open("file.log","a")
	try:
		path = "/home/madisnit/Desktop/file.py"
		info = os.lstat(path)
		major_dnum=os.major(info.st_dev)
		minor_dnum=os.minor(info.st_dev)
		dev_num=os.makedev(major_dnum, minor_dnum)
		log.write("makedev    PASS\n")
		log.close()
	except:
		log.write("makedev    FAIL\n")
		log.close()
if __name__=="__main__":	
	makedev()
