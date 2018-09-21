import os,sys
def inode():
	''' An Inode number points to an Inode. An Inode is a data structure that stores the following information about a file ,Size of file,Device ID,User ID of the file,Group ID of the file'''
	log = open("file.log","a")
	try:
		fd = os.open("/home/madisnit/Desktop/syscalls_test/8-11-2017/new.txt",os.O_RDWR|os.O_CREAT)
		info = os.fstat(fd)
		print "UID of the file",info.st_uid
		log.write("inode     PASS\n")
		log.close()	
	except:	
		log.write("inode     FAIL\n")
		log.close()
if __name__=="__main__":
	inode()
