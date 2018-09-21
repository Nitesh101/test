#!/usr/bin/python
import os
import time

processid=os.fork()
print "fork process is", processid
pid = os.getpid()
print processid ,"its pid is ", pid
ppid= os.getppid()
print pid ,"its parent pid is ", ppid
#ppid= os.getppid()
#ppid= os.getppid()
os.system("ps")
#print "fork process 1 pid, ppid"
#print "fork process 1 pid, ppid"





#print "val is " ,val

