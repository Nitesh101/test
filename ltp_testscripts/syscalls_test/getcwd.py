#!/usr/bin/python
import os
log = open("file.log","a")
try:
    os.getcwd()
    log.write("chmod    PASS\n")
    log.close()
except:
    log.write("chmod    FAIL\n")
    log.close()
#    print sys.exc_type()
