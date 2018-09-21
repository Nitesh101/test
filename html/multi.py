"""import thread
import time
def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s:%s"(threadName,time.ctime(time.time()))
def add_number(thread,*args):
	val1 = input("enter a number: ")
	val2 = input("enter a number: ")
	arg = val1+val2
	print "the add of two numbers: ",arg
try:
	thread.start.new_thread(print_time,("Thread-1",2))
	thread.start.new_thread(print_time,("Thread-2",3))
except:
	print "Error unable to start"
while 1:
	pass"""
"""import thread
import time
def prin_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s: %s"(threadName,time.ctime(time.time()))
def add_nubers(thread,*args):
	val1 = input("Enter a number: ")
	val2 = input("Enter a number: ")
	arg = val1+val2
	print "the add of two numbers: ",arg
try:
	thread.start.new_thread(print_time,("Thread-1",2))
	thread.start.new_thread(print_time("Thread-2",4))
except:
	print "Error while start"
while  1:
	pass"""

a = [(1,2),(3,4),(5,6),(7,8)]
res1 = []
for i in a:
	res = []
	for val in range(len(a)-1,-1,-1):
			res.append(val)
	tup = tuple(res)
	res1.append(tup)
print res1