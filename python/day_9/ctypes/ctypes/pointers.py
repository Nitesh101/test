#!/usr/bin/python
from ctypes import * 

class NodeStatInfo(Structure):
    _fields_ = [
        ('status', c_char * 10),
        ('name', c_char * 64)]

P_NodeStatInfo = POINTER(NodeStatInfo)
PP_NodeStatInfo = POINTER(P_NodeStatInfo)

lib = CDLL('./lib.so')
lib.cluster_info.argtypes = [c_char_p, 
                             POINTER(PP_NodeStatInfo), 
                             POINTER(c_int)]
