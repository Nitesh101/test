import os
def openfile():
		'''open a new file with open() a new file descriptor is generated, usually one more than the last file descriptor. A new entry in the file descriptor table is also provided, indexed at the file descriptor number, and a new entry is created in the open file table is generated.'''
		log=open("file.log","a")
		try:
			fd = os.open( "data.txt", os.O_RDWR|os.O_CREAT )
			os.write(fd, "This is test")
			os.close( fd )
			log.write("openfile      PASS\n")
			log.close()
		except:
			log.write("openfile     FAIL\n")
			log.close()
if __name__=="__main__":
	openfile()
print(__doc__)
