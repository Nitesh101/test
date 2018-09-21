#!/usr/bin/python

from ctypes import *

c=CDLL('./libtime.so')
c.display.restype = c_char_p
print c.display()

