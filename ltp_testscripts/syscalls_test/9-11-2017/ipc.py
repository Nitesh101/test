import socket
def ipc():
	'''Inter-Process-Communication (or IPC for short) are mechanisms provided by the kernel to allow processes to communicate with each other. On modern systems, IPCs form the web that bind together each process within a large scale software architecture'''
	log = open("file.log","a")
	try:
		if True:
			s = socket.socket()
			host=soket.gethostname()
			port = 1234
			s.bind((host, port))
			s.lsiten(5)
			while True:
				c,addr = s.accept(()
			#	print 'addr'	
			#	c.send('thamkyou for conncting')
		#		c.close()
		else:
			s = socket.socket()
			host = socket.gethostname()
			port = 1234
			s.connect((host, port))  
			print s.recv(1024)
			s.close()
			log.write("ipc      PASS\n")
			log.close()
		except:
			log.write("ipc      FAIL\n")
			log.close()
if __name__=="__main__":
	ipc()	
