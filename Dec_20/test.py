import re
fa = open("employee.txt","r")
fo = fa.read()
val = raw_input("Enter a employee name: ")
if val in fo:
	re.match(r"^[A-Z]+[a-z]+[0-9]+$",fo)
else:
	print "Error"
