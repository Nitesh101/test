import re
fil = open("file.txt","r")
fil1 = fil.readlines()
fil.close()
#print fil1
for i in fil1:
	res=re.search(r'[[A-Z a-z0-9/].+[]]',i)
	print res
