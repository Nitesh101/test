import thread
import time

def print_time(threadname, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s: %s" %( threadname, time.ctime(time.time()))
try:
	thread.start_new_thread(print_time("thread1", 2))
	thread.start_new_thread(print_time("thread2",4))
except:
	print "error"
while 1:
	pass
