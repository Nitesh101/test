import os,sys,stat
os.chmod("/home/madisnit/Desktop/oops/osconcept/one.txt",stat.S_IXGRP)

os.chmod("/home/madisnit/Desktop/oops/osconcept/one.txt",stat.S_IWOTH)
print "changed successfully"
