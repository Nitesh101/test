"""
import sys
a = sys.argv[1]
b = sys.argv[2]
sum = int(a) + int(b)
print sum

import sys
if len(sys.argv)==4:
        res = 0
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        if sys.argv[2]== '+':
                res=num1+num2
        elif sys.argv[2]== '-':
                res=num1-num2
        elif sys.argv[2]== '*':
                res=num1*num2
        elif sys.argv[2]=='%':
                res=num1%num2
        elif sys.argv[2]=='/':
                res=num1/num2
        else:
                 print "valid operator should given: "
	print "result : ",res
else:
     print "no arguments are passed"
"""
import sys
print ('append values:',len(sys.argv[1]))
print ('Listr:',str(sys.argv[2]))
