import os,sys
os.chdir("/home/madisnit/Desktop/oops/osconcept/test.txt")
print "Current working dir : %s "% os.getcwd()
fd = os.open("/tmp",os.o_RDONLY)
os.chdir(fd)
print "Current working dir: %s"% os.getcwd()
os.close(fd)
