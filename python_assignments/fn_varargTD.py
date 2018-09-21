#!/usr/bin/python
def fun1(*tup,**dic):
	print tup
	print dic				
	return


fun1(10,20,30,num=10,val=20)
fun1(10,num=10,20,val=30)

