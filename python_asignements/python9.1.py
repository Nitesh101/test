#!/usr/bin/python
import re
str1 = "john@google.com"
val2 = "(\w+)@((\w+\.)+(com))"
val = re.match(val2,str1)
print val.group(1)
