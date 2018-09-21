#!/usr/bin/python

from ctypes import CDLL
slibc = 'libc.so.6'
hlibc = CDLL(slibc)
iret = hlibc.abs(-7)
print iret
