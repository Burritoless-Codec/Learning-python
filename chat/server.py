import threading
import socket

host = "127.0.0.1"
port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nickn = []


def broadcast(message):
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nickn[index]
            broadcast(f'{nickname} has left the chat!'.encode('ascii'))
            nickn.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nickn.append(nickname)
        clients.append(client)

        print(f'New client joined: {client}, {nickname}')
        broadcast(f'{nickname} has joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening.')
receive()
