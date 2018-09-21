import thread
import time
def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s: %s"%(threadName,time.ctime(time.tima()))
def add_numbers(thread,*args):
	val1 = raw_input("Enter a number : ")
	val2 = raw_input("Enter a number: ")
	arg = val1+val2
	print "the add of two numbers: ",arg
try:
	thread.start_new_thread(print_time("Thread-1",2,))
	thread.start_new_thread(print_time("Thread-2",4,))
except:
	print "Error : unable to start thread"
while 1:
	pass
