import os
import itertools
def maximum_product_two_numbers(*args):
	list2=[]
	length=args[0]
	list1=[]
	for index in range(1,length):
		list1.append(args[index])
	for _ in range itertools.combination(list1,2):	
		list2.append(_[0]*_[1])
	print "maximum product is",max(list2)
def bit_difference(*args):
	count=0
	num1=args[0]
	num2=args[1]
#	bin1=bin(num1)
	num3=num1^num2
	bin1=bin(num3)
	for index in bin1:
		if (index=="1"):
			count+=1
	print "the numberof bits needed to flip", num1,"to",num2 ,"is",count
	return
child1=os.fork()
if child1:
	maximum_product_two_numbers(5,1,100,42,2,23)
child2=os.fork()
if child2:
	num1=input("enter number1")
	num2=input("enter number2")
	bit_difference(num1,num2)

