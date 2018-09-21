#!/usr/bin/python
import os
import time
import sys

processid = os.fork()
if (processid>0):
	print " is parent process its id :", processid , "hay am waiting 40 sec"
	time.sleep(40)

elif (processid == 0):
	ppid= os.getppid
	print "is child process its d is : ", ppid ," hey am exit"
	sys.exit(0)

print " zombie process is completed ."
sys.exit(0)


