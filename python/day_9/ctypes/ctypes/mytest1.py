#!/usr/bin/python

from ctypes import CDLL,c_double
slibm = 'libm.so.6'
hlibm = CDLL(slibm)
val = c_double(16)
print "val is ",val
print val.value
hlibm.sqrt.restype = c_double
res = hlibm.sqrt(val)
print res

base = c_double(5)
power = c_double(4)
hlibm.pow.restype = c_double
res = hlibm.pow(base,power)
print res
