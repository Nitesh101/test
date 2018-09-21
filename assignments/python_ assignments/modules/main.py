#!/usr/bin/python
import sys
import cmd_line_args_int
import cmd_line_args_str
v1=sys.argv[1]
v2=sys.argv[2]
str1=sys.argv[3]
str2=sys.argv[4]
integer=cmd_line_args_int.sumi(v1,v2)
constr=cmd_line_args_str.concat(str1,str2)

