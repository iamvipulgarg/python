from socket import *
import threading

s1=socket()
s1.bind(("localhost",1200))
s1.listen(5)
print('Waiting for Client...')
con,add=s1.accept()
print("Client Connected")

def sendMessage ():
    while True:
        msg = input("You : ")
        if msg == '':
            break
        else:
            con.send(msg.encode())

def reciveMessage ():         
    while True:
        msg=con.recv(1024)
        if msg == '':
            break
        else:
            print ("\nClient : ",msg.decode())
            
send_thread = threading.Thread(target=sendMessage)
recieve_thread = threading.Thread(target=reciveMessage)

send_thread.start()
recieve_thread.start()

send_thread.join()
recieve_thread.join()