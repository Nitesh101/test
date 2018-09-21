import os,sys
def fchdir():
	'''Change to the directory of the given file descriptor.  fildes must be
        opened on a directory, not a file.'''
    	log = open("file.log","a")
    	try:
        		os.chdir("/home/madisnit/Downloads")
			fd = os.open( "/tmp", os.O_RDONLY )
			os.fchdir(fd)
        		log.write("fchdir    PASS\n")
        		log.close()
			os.close(fd)
    	except:
        	log.write("fchdir    FAIL\n")
        	log.close

if __name__ == "__main__":
    fchdir()
