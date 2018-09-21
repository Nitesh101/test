#!/usr/bin/python

from ctypes import CDLL, c_double

slibm='libm.so.6'
hlibm=CDLL(slibm)

val=c_double(16)
hlibm.sqrt.restype=c_double
hlibm.pow.restype=c_double

print hlibm.sqrt(val)
print hlibm.pow(c_double(3),c_double(2))

nlibm=CDLL('libc.so.6')
print nlibm.abs(-78)

