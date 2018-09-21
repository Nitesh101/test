import os,sys,stat
def fchmod():
    '''Change the access permissions of the file given by file
        descriptor fd.'''
    log = open("file.log","a")
    try:
		fd = os.open("/home/madisnit/Desktop/syscalls_test/7-11-2017/test.txt",os.O_IREAD  )
		fd.write("this is new")
        	os.fchmod(fd, stat.S_IXGRP)
		os.fchmod(fd, stat.S_IWOTH)
        	log.write("fchmod    PASS\n")
        	log.close()
		os.close(fd)
    except:
        log.write("fchmod    FAIL\n")
        log.close()

if __name__ == "__main__":
    fchmod()
