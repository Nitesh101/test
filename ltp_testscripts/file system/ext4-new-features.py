import os
def ex4():
	''' it possible to mount ext3 and ext2 as ext4. This will slightly improve performance, because certain new features of ext4 can also be used with ext3 and ext2'''
	log = open("file.log","a")
	try:
		os.path.ismount("/home/madisnit/Desktop/syscalls_test/8-11-2017/new.txt")
		log.write("ex4     PASS\n")
		log.close()	
	except:	
		log.write("ex4     FAIL\n")
		log.close()
if __name__=="__main__":
	ex4()
