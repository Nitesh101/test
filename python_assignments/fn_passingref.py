#!/usr/bin/python

def fun():
	global num
	global price
	global name
	num=num+10
	price=price*2
	name='Harshita'
	print num,price,name
	return


num=100
price=500.567
name='Gangisetty'
print num,price,name	
fun()
print num,price,name	
