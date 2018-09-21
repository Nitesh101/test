import re
fopen = open("res.txt","r")
val = fopen.readlines()
#print val
fo = open("val.txt","w")
for i in val:
	a=re.findall(r'[/][a][/][a-z A-z 0-9].*[I][P]',i)
#	print a
	if a != []:
		print a,
		if a:
			fo.write(str(a))
fo.close()
fopen.close()
		
