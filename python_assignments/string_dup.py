#!/usr/bin/python

str1 = input("Enter string:")

list_temp=set(str1)
'''
ind=[]
dup_cnt=0
for index in range(len(list_temp)):
	dup_cnt=0
	for ch in list_temp:
		if ch==list_temp[index]:
			dup_cnt+=1
		if dup_cnt==2:
			ind.append(index)
print ind

for val in ind:			
	del list_temp[val]
	
print ''.join(list_temp)
			
	
'''
cnt=0
for ch in str1:
	if ch in list_temp:
		cnt+=1
	if cnt==2:
		del ch
print str1

