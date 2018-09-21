#!/usr/bin/python
import os
#import sys
log = open("file.log","a")
try:
    f=open("file.txt","r")
    os.chmod("file.txt",755) 
    f.close()
    log.write("chmod    PASS\n")
    log.close()
except:
    log.write("chmod    FAIL\n")
    log.close()
#    print sys.exc_type()
