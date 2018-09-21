import re
str1="dog cat dog"
matchobj=re.match(r'dog',str1)
if matchobj:
	print matchobj.group()
else:
	print "not matched"
search1=re.search(r'cat',str1)
if search1:
	print search1.group()
else:
	print "not matched"
find1=re.findall(r'dog',str1)
if find1:
	print find1
else:
	print "not matched"

#str2=re.sub(r'dog',str1)
