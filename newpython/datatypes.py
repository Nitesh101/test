"""
val = input("Enter a complex number: ")
val2 = input("enter a complex number: ")
print "the adding two complex numbers", val+val2
print "The subtraction of two complex numbers",val-val2
print "The divion of two complex numbers",val%val2
print "The multiplication of two complex nubers",val*val2

import math
print math.modf(100.12)
print math.sqrt(14)
print round(100)

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print cmp(list1,list2)
print len(list1)
print len(list2)
print max(list1),max(list2)
print min(list1),min(list2)
print tuple(list1)
print tuple(list2)

str1 = "nitesh"
print str1[2::]

str1 = "nitesh"
print str1+"veera"
print str1[0]
print str1[:]
print str1

import os,sys
print os.system(sys.argv[1])

str1 = input("enter a string: ")
print str1[::-1]


str1 = raw_input("enter a first string: ")
str2 = raw_input("enter a second string: ")
list1 = []
for index in range(len(str1)):
	if str1[index] == str2:
		print "Index: ",index,
		list1.append(index)
print "occurence: ",len(list1)

strn = raw_input("enter a string : ")
num = int(strn,2)
a = 1
res,val,rem = 0,0,0
octal = []
while num!=0:
	rem = num%8
	octal.append(rem)
	num/=8
octal = list(octal)
for val in octal:
	res+=val*a
	a*=10
print res

val = raw_input("enter a string: ")
val2 = "Nitesh"
print cmp(val,val2)

val = raw_input("enter a string: ")
print max(val)
print min(val)

list1 = []
val1 = input("enter a start : ")
val2 = input("enter a range: ")
for i in range(val1,val2):
	list1.append(i)
print list1

lst = input("enter a list: ")
delt = input("enter a delete element: ")
emptylist = []
emptylist = lst
del emptylist[delt]
print emptylist

val = [10,20,30,40,50,60,70,80,90,100]
print val[1:]
print val[1:4]
print val[1:9:2]
print val[1:9:1]
print val[9:1:-1]
print val[-2:-6:-1]
 

#list1 = [1,2,3,4,5]
#print len(list1)
#print list1+[6,7,8]
#print list1*3
a = 10
b = 20
list2 = [1,2,3,4,5] 
if (a in list2):
	print "value available in list1"
else:
	print "not available in list1"

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print cmp(list1,list2)
print max(list1)
print min(list2)
print len(list1)
print list1

list1 = [1,2,3,4,5]
list1.append(8)
list1.extend("nitesh")
list1.insert(0,7)
list1.pop()
list1.sort()
print list1

list1 = ['1','2','3','4','5']
print "before joining",list1
print "after joining",''.join(list1)

import random
val = random.randrange(0,10)
mylist = []
for index in range(val):
	num = random.randrange(10,20)
	mylist.append(num)
print mylist

def selection_sort(lst):
	items = len(lst)
	for index in range(items-1):
			small = index
			for index2 in range(index+1,items):
					if lst[index2]<lst[small]:
							small = index2
			if index!=small:
					lst[index],lst[small] = lst[small],lst[index]
	return lst
lst = [50,30,10,20,40]
print selection_sort(lst)

list1 = [10,30,50,80,40]
print sorted(list1)

val = input("enter a list: ")
print tuple(val)

val = input("enter a numbers: ")
print set(val)

import sys
a = sys.argv[1]
b = sys.argv[2]
sum = int(a) + int(b)
print sum
"""
import sys
if len(sys.argv)==4:
		res = 0
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[3])
		if sys.argv[2]== '+':
				res=num1+num2
		elif sys.argv[2]== '-':
				res=num1-num2
		elif sys.argv[2]== '*':
				res=num1*num2
		elif sys.argv[2]=='%':
				res=num1%num2
		elif sys.argv[2]=='/':
				res=num1/num2
		else:
				print "valid operator should given: "
		print "result : ",res
else:
	print "no arguments are passed"
