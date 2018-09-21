"""
import sys
print("python verstion")
print(sys.version_info)
import datetime
val = datetime.datetime.now()
print val

from math import pi
r  = float(input("Input the radius of the circle: "))
print str(pi*r**2)

val = raw_input("input your first name: ")
val2 = raw_input("input your last name: ")
print("Hello "+val2+" "+val)

val = raw_input("Enter a input number: ")
list = val.split(",")
tuple = tuple(list)
print list
print tuple
"""

