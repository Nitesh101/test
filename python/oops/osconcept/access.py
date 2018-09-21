import os,sys
ret = os.access("/home/madisnit/Desktop/oops/osconcept/test.txt",os.F_OK)
print ret
ret = os.access("/home/madisnit/Desktop/oops/osconcept/test.txt",os.W_OK)
print ret
ret = os.access("/home/madisnit/Desktop/oops/osconcept/tets.tct",os.R_OK)
print ret
ret = os.access("/home/madisnit/Desktop/oops/osconcept/tets.txt",os.X_OK)
print ret
