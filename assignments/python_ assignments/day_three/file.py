#!/usr/bin/python
"""
import re
fo = open("sample.csv","rb")
fa = fo.readlines()
data = raw_input("please enter what u need : ")
for val in fa:
	if re.match(data,val):
		print val.replace(',','\t')
fo.close()
"""
import threading
import time
import random
from Queue import Queue
class myThread(threading.Thread):
	def __init__(self,name,Queue):
		threading.Thread.__init__(self,name=threadname)
		self.name=name
		self.num=num
	def run(self):
		for (i%2 == 1) in range(200):
			print (self.getName(),'adding',i,'to queue')
		self.sharedata.put(i)
		time.sleep(random.randrange(10)/10.0)
		print self.getName(),'Finished'
		
class myThread1(threading.Thread):
	def __init__(self,threadname,queue):
		threading.Thread.__init__(self,name=threadname)
		self.sharedata = queue
	def run(self):
		for (i%2 == 0) in range(200):
			print self.getName(),'got avalu:',self(random.randrange(10)/10.0)
		print self.getName(),'Finished'
thread1 = mythread(name,"thread1")
thread2 = mythread1(name,"thread2")
thread1.start()
thread2.start()
