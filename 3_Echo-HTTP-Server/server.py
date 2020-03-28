#!/usr/bin/env python3

import socket
from Requests import requests
im
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 5005)
print('Starting up on port %s', server_address)
sock.bind(server_address)

sock.listen()
sendall = False
while not sendall:
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        data = connection.recv(1024)
        print('RECEIVED:', data.decode())
        request = requests(data.decode())
        if data:
            print('Sending data back to the client')
            connection.sendall(data)
            sendall = True
        else:
            print('No more data from', client_address)
            break

    finally:
        connection.close()