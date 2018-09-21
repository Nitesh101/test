import socket
s = socket.socket()
host = socket.socket()
port = 12345
s.bind((host, port))
s.listen(5)
