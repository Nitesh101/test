import socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostname()
client_sock.connect((ip,5001))
client_sock.send("votary")
str1=client_sock.recv(10240)
print "data from server",str1
client_sock.close()
