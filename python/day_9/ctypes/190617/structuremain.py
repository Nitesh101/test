#!/usr/bin/python

from ctypes import *

class STUDENT(Structure):
    _fields_ = [("id",c_int),
                ("marks",c_float)]

Student = STUDENT(c_int(112),c_float(50.69))
print "ID:",Student.id," MARKS:",Student.marks


