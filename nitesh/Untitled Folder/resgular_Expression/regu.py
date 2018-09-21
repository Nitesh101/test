import re
f = open("file.txt","r")
a = f.readlines()
f.close()
for i in a:
	res=re.search(r"[[a-z A-Z 0-9/].+[]]",i)
	print res.group()
