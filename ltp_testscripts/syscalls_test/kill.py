#!/usr/bin/python
import os,signal
log = open("file.log","a")
try:
	os.system("pkill -9 iChat")
	log.write("kill PASS\n")
	log.close()
except:
    log.write("kill    FAIL\n")
    log.close()
#    print sys.exc_type()
