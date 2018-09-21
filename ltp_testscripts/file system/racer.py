import os.path
def racer():
	'''deletes, and recreates them as fast as possible.  This is all done in
## an effort to test for race conditions in the filesystem code. This test
## runs until killed or Ctrl-C'd.  It is suggested that it run overnight
## with preempt turned on to make the system more sensitive to race.'''
	log = open("file.log","a")
	try:
   		os.listdir(os.getcwd())
		if os.path.isfile("/home/madisnit/Desktop/syscalls_test/9-11-2017/ni.txt"):
			os.remove("/home/madisnit/Desktop/syscalls_test/9-11-2017/ni.txt")
		else:	
			os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
			log.write("racer       PASS\n")
			log.close()
	except:
		log.write("racer        FAIL\n")
		log.close()
if __name__=="__main__":
	racer()
