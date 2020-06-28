import socket 
import ssl 
import datetime

print ('pokretanje')
tim1 =datetime.datetime.now()
print (tim1)
client_socket = socket.socket()
host = "localhost"
port=7000
print(host)

ssl_client_socket = ssl.wrap_socket(client_socket, ca_certs="cert.pem", cert_reqs = ssl.CERT_REQUIRED)

ssl_client_socket.connect((host,port))
print (ssl_client_socket.recv(1024))
ssl_client_socket.close()
t2 =datetime.datetime.now()
total = t2-tim1
print ('skeniranje %s min ' %(total))