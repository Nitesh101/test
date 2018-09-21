import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if 1:
	data="HELLO"
	client_socket.sendto(data, ("localhost",6666))
	print "Sending request"
	recv_data, addr = client_socket.recvfrom(256)
	print "time :",recv_data
	
client_socket.close()

