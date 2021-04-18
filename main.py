import os
import socket
import threading
import platform
if platform.system() == 'Windows':
    os.system("cls")
    print("\t\t\tCHAT APP USING UDP PROTOCOL")
    os.system("color 6")
else:
    os.system("clear")
    print("\t\t\tCHAT APP USING UDP PROTOCOL")
    os.system("tput setaf 6")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client_valid = False
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print(ip)
print(type(ip))
while not client_valid:
    client = input("\nAre you client A or client B? Enter A or B: ")
    if client == "A" or client == "a":
        port = 1234
        sendip = input("\n\t\tEnter client B's IP: ")
        sendport = 4321
        client_valid = True
    elif client == "B" or client == "b":
        port = 4321
        sendip = input("\n\t\tEnter client A's IP: ")
        sendport = 1234
        client_valid = True
    else:
        print("\nInvalid input! please try again!")

print(sendip)
print(type(sendip))

s.bind((ip, port))

def recieve():
    while True:
      x = s.recvfrom(1024)
      print(f"\n\t\t\t{sendip} : {x[0].decode()}" )
       
def send():
    while True:
      x = input("")
      s.sendto(x.encode(), (sendip, sendport))
        
recieve = threading.Thread( target=recieve )
send = threading.Thread( target=send )

recieve.start()
send.start()
