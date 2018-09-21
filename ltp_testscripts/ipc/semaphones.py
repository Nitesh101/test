import threading
def semaphones():
	'''Semaphores are locking and synchronization mechanism used most widely when processes share resources'''
	log=open("file.log","a")
	try:
		x      = 0                   # A shared value
		x_lock = threading.Lock()    # A lock for synchronizing access to x
		COUNT = 1000000
		def foo():
    			global x
    		for i in xrange(COUNT):
        		with x_lock:
            			x += 1

		def bar():
    			global x
    		for i in xrange(COUNT):
        		with x_lock:
            			x -= 1
		t1 = threading.Thread(target=foo)
		t2 = threading.Thread(target=bar)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		log.write("semaphones      PASS\n")
		log.close()
	except:
		log.write("semaphones       FAIL\n")
		log.close()

if __name__=="__main__":
	semaphones()
 
