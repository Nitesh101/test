#!/usr/bin/python

from ctypes import *
import sys

c=CDLL('./libpointer.so')

#c.get_address.restype = c_int

try:
    c.set_value(c_int(int(sys.argv[1])))
except:
    print "USAGE : ./pointermain <int value>"
    sys.exit(0)

print c.get_address()

