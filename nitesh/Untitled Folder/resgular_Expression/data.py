import re
f = open("new.txt")
val = f.readlines()
#print val
for i in val:
	res = re.findall(r"@\w.+\S",i)
	print res
