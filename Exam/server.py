import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostname()
sock.bind((ip,5005))
sock.listen(5)
client,addr = sock.accept()
data = client.recv(1024)
str1 = data
print str1
client.send(str1)
sock.close()
