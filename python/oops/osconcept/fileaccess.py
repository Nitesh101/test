import os,sys
res = os.access("/home/madisnit/Desktop/oops/osconcept/one.txt",os.F_OK)
print res
res = os.access("/home/madisnit/Desktop/oops/osconcept/one.txt",os.R_OK)
print res
res = os.access("/home/madisnit/Desktop/oops/osconcept/one.txt",os.W_OK)
print res
res = os.access("/home/madisnit/Desktop/oops/osconcept/one.txt",os.X_OK)
print res
