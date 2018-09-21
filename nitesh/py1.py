"""#!/usr/bin/python
list1=[[1,2],[3,4],[5,6]]
list2=[]
list3=[]
for i in range(0,len(list1)):
	list3=list1[i]
	for j in list3:
		list2.append(j)
print list2	


s1="python"
s2=s1
s2.replace("p","j")
print s1,s2


l=[1,2,3,4]
l1=l
l2=l[:]
l1.append(5)
print l
print l1
print l2
"""

list1=[1,3,2,4]
for val in range(0,len(list1)-1):
	for v1 in range(1,len(list1)):
		if val>v1:
			print val
	   
