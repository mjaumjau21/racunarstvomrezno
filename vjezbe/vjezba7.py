import datetime
import sys
import socket
import multiprocessing
import os
def port_scanner(param):
     targetIP, PortNumber = param
     tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     rezultat = tcp_sock.connect_ex((targetIP,PortNumber))
     if rezultat == 0:
         return PortNumber, True
     else:
         return PortNumber, False

     tcp_sock.close()

def ispis():
     print ('pokretanje')
     print (datetime.datetime.now())
     print ('program se izvodi')
def handler(ports):
     CoreNum = multiprocessing.cpu_count()
     print ("broj core-ova ovog procesora je %d te cemo kreirat  %d procesa" % (CoreNum, CoreNum*2))
     pool = multiprocessing.Pool(processes=CoreNum*2)
     for port, status in pool.map(port_scanner, [(targetIP,port) for port in ports]):
         print ("Skeniram port: %d" % (port))
         if status == True:
             print ("port %d je otvoren" %(port))
         else:
             print ("port zatvoren %s" %(port))
if __name__ == '__main__':
	print ('unesite adresu')
	target =input(">> ")
	try:
		targetIP = socket.gethostbyname
		print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
		print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
		var = os.system('ping ' + targetIP + ' -n ')
		if var == 0:
			start =input("Pocetni port >> ")
			end =input("Zavrsni port >> ")
			start_time = datetime.datetime.now()
			ports = range(int(start),int(end)+1)
			handler(ports)
			elapsed_time = datetime.datetime.now() - start_time
			print ("Skeniranje portova zavrseno!")
			print ("Vrijeme trajanja: %s "% (elapsed_time))
		else:
			print("." * 50)
			print ("Host %s nije dostupan. Program se zavrsava!" %host)
	except socket.gaierror:
		print ('zapis nije u dns')