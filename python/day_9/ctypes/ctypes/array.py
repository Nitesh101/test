#!/usr/bin/python 

import ctypes as ct

lib = ct.CDLL('./array.so')
my_array_type = ct.c_int * 5
my_array = my_array_type()
my_array[0:5] = [0, 1, -2, 3, 10]     
lib.multiply_array.argtypes = (ct.POINTER(ct.c_int), ct.c_int)
lib.multiply_array.restype = None 
my_array_ptr = ct.cast(my_array, ct.POINTER(ct.c_int))
lib.multiply_array(my_array_ptr, 5)
for i in range(5):
    print(my_array[i]),
