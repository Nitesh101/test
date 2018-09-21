#!/usr/bin/python
"""
import sys
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)



#/!usr/bin/python

import sys
print "command line argument are: ",
total_nums = len(sys.argv)
if total_nums > 1:
	for index in range(1,total_nums):
		num = (sys.argv[index])
		if num.isdigit():
			print num ,"it is number"
		
		elif num.isalpha():
			print num  ,"it is string"

else:
	print ("No argument passed")
 
"""
import sys
from sum_num import sumNum
from stringadd import addString

if len(sys.argv) == 1:
        print("Pass cmd arguments (either num or string)")
else:
        count = 0
        for val in sys.argv[1:]:
                if val.isdigit():
                        count += 1
                        pass
                else:
                        break
        else:
                sumNum(sys.argv[1:])

        if count == 0:
                if all(isinstance(e, str) for e in sys.argv[1:]):
                        for val in sys.argv[1:]:
                                if val.isdigit():
                                        print("Pass cmd arguments (either num or string)")
                                        sys.exit()
                        addString(sys.argv[1:])
                else:
                        print("Pass cmd arguments (either num or string)")

