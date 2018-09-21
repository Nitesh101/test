#!/usr/bin/python
import os
#import sys
log = open("file.log","a")
try:
    f=open("file.txt","r")
    os.chdir("file.txt")
    f.close()
    log.write("chdir    PASS\n")
    log.close()
except:
    log.write("chdir    FAIL\n")
    log.close
#    print sys.exc_type()
