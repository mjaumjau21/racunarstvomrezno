import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 4123
MESSAGE = 'Slavko Škorić'
print('UDP IP:', UDP_IP)
print('UDP port:', UDP_PORT)
print('porka:', MESSAGE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(bytes(MESSAGE, 'utf-8'), (UDP_IP, UDP_PORT))