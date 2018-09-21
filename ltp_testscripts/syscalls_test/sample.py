#!/usr/bin/python
import os

def fnamesize():
    fname = "a" * 255
    log = open("fs.log","a")
    try:
        with open(fname,"w") as F:
            F.write("some data")
        F.close()
        log.write("fnamesize    PASS\n")
        log.close()
        os.remove(fname)
    except:
        log.write("fnamesize    FAIL\n")
        log.close

if __name__ == "__main__":
    fnamesize()
