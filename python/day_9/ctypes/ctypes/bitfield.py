#!/usr/bin/python
import ctypes

c_short = ctypes.c_short

class Flags_bits(ctypes.LittleEndianStructure):
    _fields_ = [("bitField1", c_short, 1),
                ("bitField2", c_short, 4),
                ("bitField3", c_short, 6),
                ("bitField4", c_short, 1),
                ("bitField5", c_short, 2),
                ("bitField6", c_short, 2),
                ("bitField7", c_short, 6),
                ("bitField8", c_short, 4),
                ("bitField9", c_short, 4),
                ("bitField10", c_short, 1),
                ("bitField11", c_short, 1)]


for field_descr in Flags_bits._fields_:        
    name = field_descr[0]
    field = getattr(Flags_bits, name)    
    bfield_bits = field.size >> 16    
    if bfield_bits:
        start = 8 * field.offset + field.size & 0xFFFF
        stop = start + bfield_bits
    else:
        start = 8 * field.offset
        stop = start + 8 * field.size
    print("{:>10s}: bits {:>2d}:{:>2d}".format(
          name, start, stop))
