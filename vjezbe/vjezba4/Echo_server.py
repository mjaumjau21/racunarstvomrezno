import socket
host = socket.gethostname()
port = 12233
echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)
print ('klijent...')
conn, addr = echo_server.accept()
print ('spojen', addr)
while True:
	data = conn.recv(1024)
	if not data: break
	conn.sendall(data)
conn.close()