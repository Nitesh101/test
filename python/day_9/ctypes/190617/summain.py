#!/usr/bin/python

from ctypes import *

c=CDLL('./libsum.so')

c.sum.restype = c_int
arr= c_int * 5
a=arr(2,1,2,1,1)

res=c.sum(a,c_int(len(a)))

print res
