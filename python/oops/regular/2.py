import re
lst = ['8005551212','8005551212','9992341255','7013026781','9825162310'] 
for i in lst:
	if re.match(r"[9,7,8]{1}[0-9]{9}",i and len(i) == 10):
		print "yes"
	else:
		print "no"
		
