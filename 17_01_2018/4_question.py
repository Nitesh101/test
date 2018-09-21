#!/usr/bin/python
val = raw_input("Enter string: ")
count = 0
for i in val:
	if i in val[val.index(i)+1:]:
		pass
	else:
		print "irst non-repeating charecter string:",val,"is",i
		count += 1
		break
if count == 0:
		print "first non-repeatinf charecter string",val,"is","-1"

