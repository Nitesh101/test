#!/usr/bin/python 

class Int(Structure):
	_fields_ = [("first_16", c_int, 16),("second_16", c_int, 16)]

print Int.first_16

print Int.second_16
