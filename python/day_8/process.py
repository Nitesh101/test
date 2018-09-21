#!/usr/bin/python
import os,time,sys
pid=os.fork()
if ( pid >0):
	print("get the Pid of the parent: ",pid)
	#time.sleep(10)
	#os.wait()
else:
	time.sleep(10)
	os.wait()
sys.exit(0)
