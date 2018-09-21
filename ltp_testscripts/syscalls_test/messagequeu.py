import Queue
def messagequeue():
	'''Message Queues are synonymous to mailboxes. One process writes a message packet on the message queue and exits. Another process can access the message packet from the same message queue at a latter point in time'''
	log = open("file.log","a")
	try: 
		q = Queue.Queue()
		for x in range(4):
    			q.put("item-" + str(x))
		while not q.empty():
			 q.get()
		log.write("message       PASS\n")
		log.close()
	except:
		log.write("message       FAIL\n")
		log.close()
if __name__=="__main__":
	messagequeue()
 
