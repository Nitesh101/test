import re
fil = open("file.txt","r")
fil1 = fil.readlines()
#print fil1
fil.close()
for i in fil1:
	if re.search(r'[a-z,A-Z,0-9]',fil1):
		print i
