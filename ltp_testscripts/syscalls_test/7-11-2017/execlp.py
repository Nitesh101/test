#!/usr/bin/python
import os

def execlp():
	args = ['write','this','out']
    log = open("file.log","a")
    try:
		#args = ['write','this','out']
		os.execlp("echo", *args)
       	 	log.write("execlp    PASS\n")
        	log.close()
    except:
        log.write("execlp    FAIL\n")
        log.close()

if __name__ == "__main__":
    execlp()
