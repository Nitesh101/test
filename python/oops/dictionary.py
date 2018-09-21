"""
dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
for key,value in sorted(dict.items()):
	print key,value


for i,j in dict.items():
	print i,j

print dict['Name']
print dict['Age']

dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
dict2 = {102:'sanjoy'}
dict.update(dict2)
print dict
print dict2

dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
data = {}
data = data.fromkeys(dict)
print data

dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
data = sorted(dict.values())
print data
dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
d = dict.fromkeys(dict,10)
print d

dict = {'Name' : 'nitesh', 'Age' : 30, 'id' : 10}
sorted(dict, key=lambda dict:dict[0])
print dict
"""
from operator import itemgetter
a = [{"id":1,"data":{"age":16,"name":"a"}}, 
     {"id":3,"data":{"age":35,"name":"b"}}, 
     {"id":2,"data":{"age":9,"name":"c"}}]
l = sorted(a,key=lambda k: itemgetter('age')(itemgetter('data')(k)))
print l
