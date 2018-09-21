list1 = [1,13,7,5,9]
"""
for i in range(0,len(list1)):
	for j in range(i+1,len(list1)):
		if i+j == 14:
"""

for i in range(len(list1)):
	for j in range(1,len(list1)-1):
		if i+j == 14:	
			print i,j
"""
	if i+j == 14:
		print i,j
"""
