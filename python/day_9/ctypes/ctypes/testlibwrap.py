#!/usr/bin/python

import ctypes

testlib = ctypes.CDLL('/home/alvalsan/linux_adv/ctypes/testlib.so')
testlib.myprint()
