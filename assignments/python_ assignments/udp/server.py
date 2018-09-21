import socket
import time
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
server_socket.bind(('', 6666))

print "UDPServer Waiting for client on port 6666"

if True:
	dataFromClient, address = server_socket.recvfrom(256)
	print "receving data is    :",dataFromClient
	epochTime = str(time.time())
	print "time ;",epochTime
	server_socket.sendto(epochTime, address)

