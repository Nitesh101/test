import socket
server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostname()
server_sock.bind((ip,5001))
server_sock.listen(5)
client,addr=server_sock.accept()
data=client.recv(10240)
print "data from client is",data
list1=[]
list2=[]
for index in data:
	list1+=index
str1=""
str1=data[::-1]
#print "list2",list2
#print "list1",list1
#for index in list2:
#	str1.join(index)
print str1
client.send(str1)
server_sock.close()

