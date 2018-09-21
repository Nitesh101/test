import os
def acl():
	'''Files and directories have permission sets for the owner of the file, the group associated with the file, and all other users for the system.'''
	log = open("file.log","a")
	try:
		f=os.access("new.txt",os.R_OK)
		#fa=os.write(f,"this is new line")
		log.write("acl     PASS\n")
		log.close()	
	except:	
		log.write("acl     FAIL\n")
		log.close()
if __name__=="__main__":
	acl()
