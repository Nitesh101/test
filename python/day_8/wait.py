#!/usr/bin/python
import os
import time
import sys

processid = os.fork()
if (processid>0):    
	print " is parent process its id :", processid , " waiting 15 sec for child"
	os.wait()

elif (processid == 0):
	time.sleep(15)
	ppid= os.getppid()
	print "is child process its is : ", ppid ," thank you for wait"
	sys.exit(0)

print " "
sys.exit(0)


