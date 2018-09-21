import threading
import sys
class myThread(threading.Thread):
	global_val=2
	def __init__(self,num,name):
		threading.Thread.__init__(self)
		self.name=name
		self.num=num
	def run(self):
		threadlock.acquire()
		print "starting" +self.name
		addition(self.num)
		print "ending" +self.name
		threadlock.release()
def addition(num):
	count=myThread.global_val
	for index in range(count):
		num=num+num
	print "the num after increment is",num
	return
threadlock=threading.Lock()
if len(sys.argv) <= 1:
	num=100000
else:
	num=sys.argv[1]
threads=[]
thread1=myThread(num,"thread1")
thread2=myThread(num,"thread2")
thread1.start()
thread2.start()
threads.append("therad1")
threads.append("therad2")
#for t in threads:
#	t.join()
