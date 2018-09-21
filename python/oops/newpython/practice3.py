"""
str1 = "W3RESOURCE"
print str1[:4].lower()+str1[4:]

str1 = "nitesh is good boy"
print (str1.split(' '))
"""
def count_dict(mystring):
	d = {}
	for i in mystring:
		d[i]=mystring.count(i)
count_dict("niteshtes")
