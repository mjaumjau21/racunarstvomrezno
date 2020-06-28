import socket, datetime
import sys

print ("Vrijeme pokretanja : ")

time1 =datetime.datetime.now()

print (time1)
host = socket.gethostname()
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
print("Unesite ime i prezime")
message = input()

def Main():

    while True: 
        s.send(message.encode('ascii'))
        data=s.recv(1024)
    
        print('Received from the server: ' , str(data.decode('ascii')))
    
        ans=input('Napisite exit da izadete iz programa:  ')
        if ans =='exit':
            print("Bye")
            break
        else:
            continue
        s.close()

if message =='Slavko Skoric':
    Main()
else:
    print("Wrong input")
    sys.exit()