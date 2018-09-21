#!/usr/bin/python
import os
import time
import sys

processid = os.fork()
ppid=os.getppid()
if (processid>0):
	print " is parent process its id :", ppid
	sys.exit(0)
elif (processid == 0):
	time.sleep(10)
	pid =os.getpid() 
	print "child process its d is : ", pid


print "parent id", processid
sys.exit(0)
	

