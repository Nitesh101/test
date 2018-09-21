import os,sys,stat
def acls():
	'''ACL entries consist of a user (u), group (g), other (o) and an effective rights mask (m). An effective rights mask defines the most restrictive level of permissions. setfacl sets the permissions for a given file or directory. getfacl shows the permissions for a given file or directory. .'''
	log = open("file.log","a")
	try:
		os.chmod("new.txt",stat.S_IXGRP)
		#fa=os.write(f,"this is new line")
		log.write("acls     PASS\n")
		log.close()	
	except:	
		log.write("acls     FAIL\n")
		log.close()
if __name__=="__main__":
	acls()
