"""
d = {0:10,1:20}
d[2]=30
print d

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print dic1

val = raw_input("Enter a dic: ")
d = {'name':'nitesh','id':20,'age':25}
if val in d:
	print ("key is present in dicrionary")
else:
	print("key is not present")

d = {'x':10,'y':20,'z':30}
for i,j in d.items():
	print j

n = int(input("Input a number: "))
d = dict()
for x in range(1,n+1):
	d[x]=x*x
print d

val = int(input("Input a number: "))
d = dict()
for x in range(1,val+1):
	d[x]=x*x
print d

d={}
for x in range(1,16):
	d[x]=x**2
print d

d1 = {'a':100, 'b':200}
d2 = {'x':400 , 'y':600}
d1.update(d2)
print sorted(d1.items())

dic = {'data1':100,'data2':200,'data':300,'data3':100}
print sum(dic.values())

dic = {'a':10,'b':20,'c':30,'d':40}
del dic['a']
print dic
"""
keys  = ['red','green','blue']
values = ['#FF0000','#008000','#227783']
d = dict(zip(keys,values))
print d
