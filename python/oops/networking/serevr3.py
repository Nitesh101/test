import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
	c, addr = s.accept()
	print "got connection"
	c.send("Thankyou for connecting")
	c.close()

