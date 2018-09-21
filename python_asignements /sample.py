"""
#lst=[1, -1, 3, 2, -7, -5, 11, 6 ]
lst = [-5, 7, -3, -4, 9, 10, -1, 11]    
#lst = input("Enter a values: ")
op = []
index=0
for val in lst:
    if val > 0:
        op.insert(index, val)
        index += 1
    else:
        op.append(val)
        
print op
"""
lst = [-5, 7,-3, -4, 9, 10, -1, 11]
l1=[]
index = 0
for val in lst:
	if val > 0:
		l1.insert(index,val)
		index+=1
	else:
		l1.append(val)
print l1
