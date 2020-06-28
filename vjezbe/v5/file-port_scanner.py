import datetime
import socket
import time

start_time = time.time()

print ("program pokrenut u: ")
print (datetime.datetime.now())
print ("adresa hosta za testiranje ")
target = input(">>")
targetIP = socket.gethostbyname(target)

print ("host skeniran: %s, ip adresu: %s" % (target, targetIP))
print ("port za skeniranje?")
start = int(input("pocetni port"))
end = int(input("zavrsni port"))

for Port in range(int(start),int(end)+1):
	sock = socket.socket()
	result = sock.connect_ex((targetIP,Port))
	if result == 0:
		print("port %s " %(Port))
	else:
		print ("port zatvoren %s" %(Port))
	sock.close()

elapsed_time = time.time() - start_time

print ("skeniranje završeno")
print ("trajanje %s " %elapsed_time)