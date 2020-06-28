#tcp_server.py
import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 5000
server_socket.bind((host,port))
print("Cekanje")
server_socket.listen(5)
msg = "Halo"
byt = msg.encode()
while True:
	conn,addr = server_socket.accept()
	print("Konekcija %s" %str(addr))
	conn.send(byt)
	conn.close()