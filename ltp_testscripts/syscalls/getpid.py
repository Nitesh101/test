#!/usr/bin/python
import os
log = open("file.log","a")
try:
    os.system("ps")
    log.write("getpid    PASS\n")
    log.close()
except:
    log.write("getpid    FAIL\n")
    log.close()
#    print sys.exc_type()
