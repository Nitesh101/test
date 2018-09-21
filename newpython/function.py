"""
def fun(list1):
	res=0
	for val in list1:
			res=res+val
	print res
	return
list1=[1,2,3,4,5]
fun(list1)
print l
"""
"""
val = input("enter a string: ")
temp = []
temp2 = []
for i in val:
	if i.upper():
		temp.append(i)
	elif i.lower():
		temp2.apeend(i)
print temp
print temp2

value = raw_input("enter a string: ")
temp  = []
temp2 = []
for i in value:
	if i.isupper() == True:
		temp.append(i)
	elif i.islower() == True:
		temp2.append(i)
print ("The upper case letters",temp)
print ("Thes lower case letters",temp2)


str1 = "NItesh"
print str1.upper();
print str1.lower();

def fun(*tup):
	res = []
	cnt=0
	length=len(tup)
	while(cnt<length):
		temp=0
		for val in tup[cnt]:
			temp=temp+val
		res.append(temp)
		cnt+=1
	return res
tup=(1,2,3,4,5)
tup1=[10,20,30,40]
res=fun(tup,tup1,tup)
print res
"""
