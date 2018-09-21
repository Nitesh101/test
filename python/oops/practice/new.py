"""def sum_list(lis):
	count = 0
	for i in lis:
		count += i
	return count
print(sum_list([1,2,3,4]))
def mul_lis(lis):
	count = 0
	for i in lis:
		count+=i
	return count
print(mul_lis([1,2,3]))]
def max_num_in_list( list ):
    count = 0
    for i in list:
    	if i > count:
    		count = i
    return count
print(max_num_in_list([1,2,5,6]))
from operator import itemgetter
lis = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lis2 = sorted(lis,key=itemgetter(1))
print lis2
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(d.items(),key=operator.itemgetter(0))
print sorted_d
sorted_d = sorted(d.items(),key=operator.itemgetter(0).reverse=True)

d = {0: 10, 1: 20}
d.update({6:40})
print d
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key(x):
	if x in d:
		print("keys is present in dictionary")
	else:

		print("key is not present in dictionary")
is_key(5)
n=5
d={}
for i in range(1,n+1):
	d[i]=i*i
print d

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print d
d1 = {'a': 100, 'b': 200}
result = 1
for key in d1:
	result=result*d1[key]
print result
d1 = {'a': 100, 'b': 200}
result = 0
for key in d1:
	result=result+d1[key]
print result
d1 = {'a': 100, 'b': 200}
print d1
if 'a' in d1:
	del d1['a']
print d1

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
colour = dict(zip(keys,values))
print colour

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

print filtered_list

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))
print mapped_list

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)
print reduced_list
lamda =  lambda x: x * x
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
for key in sorted(color_dict):
	print(key,color_dict[key])

my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys(),key=(lambda k: my_dict[k]))
print my_dict[key_max]

my_dict = {'x':500, 'y':5874, 'z': 560,'x':500}
print my_dict
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1)+Counter(d2)
print d
class Animal:
	def eat(Self):
		print "Eatining"
class Dog(Animal):
	def bark(Self):
		print "Barking"
d = Dog()
d.eat()
d.bark()

#Multilevel
class Animal:
	def eat(Self):
		print "eatting"
class dog(Animal):
	def bark(Self):
		print "barking"
class Babydog(dog):
	def weep(Self):
		print "weeping"
d  = Babydog()
d.eat()
d.bark()
d.weep()

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key,value) in set(x.items()) & set(y.items()):
	print key,value

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)
from collections import defaultdict,Counter
str1 = 'w3resource'
my_dict = {}
for letter in str1:
	my_dict[letter]=my_dict.get(letter,0)+1
print my_dict

class call():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		return self.a+self.b
	def mul(self):
		return self.a*self.b
b = call(4,5)
print b.add()
print b.mul()
"""
val = [2,3,4,8,1,10]
for i in range(0,len(val)):
	for j in range(i+1,len(val)):
		if val[i]>val[j]:
			break
	print val[i]


















