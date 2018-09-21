import re
fa = open('number.txt','r')
#fb = fa.readlines()
for i in fa:
	if re.match(r"(\w+)(:)(/d+)",i):
			print i,
