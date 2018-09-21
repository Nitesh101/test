import socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostname()
sock.connect((ip,5005))
sock.send("votary.com")
str1 = sock.recv(1024)
#print str1
sock.close()	
