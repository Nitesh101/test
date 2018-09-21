import os,time
def fork():
	'''fork - create a child process'''
	log = open("file.log","a")
	try:
		pid = os.fork()
		print "pid %d"%pid
		log.write("fork  PASS\n")
		log.close()
	except:
		log.write("fork  FAIL\n")
		log.close()
if __name__=="__main__":
	fork()
