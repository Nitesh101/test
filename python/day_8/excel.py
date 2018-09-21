#!/usr/bin/python
import os
args=["this","out"]
print args
os.execlp("echo",*args)
