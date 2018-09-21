#l = [1,2,3,'python',5,6,'string']
l = [1,2,3,4,5]
count = 0
for i in l:
	if type(i) == int:
		count += 1
print count
"""
intcount,strcount = 0,0
for i in l:
	if type(i) == int:
		intcount += 1
	elif type(i) == str:
		strcount += 1
print intcount,strcount
"""
