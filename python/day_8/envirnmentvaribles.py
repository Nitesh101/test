#!/usr/bin/python
import os
def Main():
	os.system("v1=10")
	pid = os.fork()
	if(pid==0):
		print "PPID=",os.getppid()
		print os.system("echo $v1")
	else:
		
		print "parent PID=",os.getpid()
		os.wait()
if __name__ == "__main__":
	Main()
