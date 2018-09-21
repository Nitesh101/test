import os,sys
def fs_perms():
	'''his file contains a list of files and directories with known permissions.It is used by the packaging class to ensure that the permissions,owners and,group of listed files and directories are in sync across the system.'''
	log = open("file.log","a")
	try:
		os.access("new.txt",os.R_OK)
		log.write("fs_perms       PASS\n")
		log.close()
	except:
		log.write("fs_perms        FAIL\n")
		log.close()
if __name__=="__main__":
	fs_perms()
