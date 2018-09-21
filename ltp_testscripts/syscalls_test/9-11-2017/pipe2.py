import cPickle

import os

#communicate with another process through named pipe

#one for receive command, the other for send command
def pipe():

	log = open("file.log","a")
	try:
		wfPath = "/home/madisnit/Desktop/syscalls_test/9-11-2017/new.txt"
		rfPath = "/home/madisnit/Desktop/syscalls_test/9-11-2017/new2.txt"
		wp = open(wfPath, 'w')
		wp.write("P1: How are you?")		
		wp.close()
		rp = open(rfPath, 'r')
		response = rp.read()
		#print "P1 hear %s" % response
		rp.close()
		wp = open(wfPath, 'w')
		wp.write("P1: I'm fine too.")		
		wp.close()
		log.write("pipe    PASS\n")
		log.close()
	except:
		log.write("pipe    FAIL\n")
		log.close()
if __name__=="__main__":	
	pipe()
