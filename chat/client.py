import threading
import socket


#Getting user to select a nickname.
nickname = input('Please type a nickname: ')


#define ip and port that server should be on.
host = "127.0.0.1"
port = 65432

#creating the connection to the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#setup for receiving data from server and other clients.
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            #checks to see if server is asking for a nickname or sending other data
            #does not validate if said nickname is available or not.
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        #connection failing correctly?!?
        except:
            print('Task failed successfully')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input('')}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
