import os,sys
def link():
	'''Create a hard link to a file.'''
	log = open("file.log","a")
	try:
		path = "/home/madisnit/Desktop/file.py"
		fd = os.open( path, os.O_RDWR|os.O_CREAT )
		os.close(fd)
		dst = "/home/madisnit/Downloads/file.py"
		os.link(path,dst)
		log.write("link    PASS\n")
		log.close()
	except:
		log.write("link    FAIL\n")
		log.close()
if __name__=="__main__":	
	link()
