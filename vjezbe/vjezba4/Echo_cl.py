import socket 
host = socket.gethostname()
port = 12233
client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.sendall("test serv")
data = client_socket.recv(1024)
print (data)
client_socket.close()
print (datetime.datetime.now())