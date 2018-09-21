#!/usr/bin/pyhton
import threading
import time
class printnums(threading.Thread):
	def __init__(self,start_num,end_num,step,step_event,clear_event):
		threading.Thread.__init__(self)
		self.start_num=start_num
		self.end_num=end_num
		self.step=step
		self.step_event=step_event
		self.clear_event=clear_event
	def run(self):
		for i in range(self.start_num,self.end_num,self.step):
			print(i)
			self.step_event.set()
			self.clear_event.clear()
			self.clear_event.wait()
		self.step_event.set()
threading_event1=threading.Event()
threading_event2=threading.Event()
t1=printnums(0,20,2,threading_event1,threading_event2)
t2=printnums(1,20,2,threading_event2,threading_event1)
t1.start()
t2.start()
t1.join()
t2.join()
