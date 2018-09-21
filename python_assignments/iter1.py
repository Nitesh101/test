#!/usr/bin/python
'''
list1=input("Enter a list:")
itr= iter(list1)

while True:
	try:
		print itr.next()
	except StopIteration:
		break	
'''
'''
tup=input("Enter a tuple:")
itr=iter(tup)

while True:
	try:
		print itr.next()
	except StopIteration:
		break
'''

dic=input("Enter a dictionary:")


itr=iter(dic)
while True:
	try:
		key= itr.next()
		print dic[key]
	except StopIteration:
		break


itr=iter(dic.values())
while True:
	try:
		print itr.next()
	except StopIteration:
		break

		
