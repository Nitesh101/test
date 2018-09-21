import re
f=open('two.txt','r')
data=f.read()

matchObj = re.match( r'cats (.*) dogs', data,re.I|re.M)
if matchObj:
	print matchObj.group(1)
else:
	print "No match!!"
