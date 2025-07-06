from socket import *
import threading

s1=socket()
s1.connect(("localhost",1200))

print("REQ Send")

def sendMessage ():
    while True:
        msg = input("You : ")
        if msg == '':
            break
        else:
            s1.send(msg.encode())
        
def reciveMessage ():  
    while True:
        msg=s1.recv(1024)
        if msg == '':
            break
        else:
            print("\nServer: ",msg.decode())


send_thread = threading.Thread(target=sendMessage)
recv_thread = threading.Thread(target=reciveMessage)

send_thread.start()
recv_thread.start()

send_thread.join()
recv_thread.join()