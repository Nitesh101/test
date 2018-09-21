#!/usr/bin/python

from ctypes import *

class FLAGS(Structure):
    _fields_ = [("flag5",c_int,5),
                ("flag6",c_int,6)]

print FLAGS.flag5
print FLAGS.flag6
