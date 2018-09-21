#!/usr/bin/python 

import ctypes as ct
lib = ct.CDLL('./mylib.so')
lib.mysum.argtypes = (ct.c_int, ct.c_int) # input are two ints
lib.mysum.restype = ct.c_int              # return value is also int
a = lib.mysum(3, 4)
print(a)
