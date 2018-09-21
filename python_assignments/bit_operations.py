#!/usr/bin/python

val1=input("Enter valuein decimal:")
pos= input("Enter position to edit:")
set1=val1 | (1<<pos)
print bin(set1)
clr1=val1 & (~(1<<pos))
print bin(clr1)
tog=val1 ^ (1<<pos)
print bin(tog)
