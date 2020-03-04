#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 52186

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as msocket:
    msocket.bind((HOST, PORT))
    msocket.listen()
    connection, address = msocket.accept()
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)
            if data:
                print('Message received: ', repr(data))
            else:
                break
            connection.sendall(b'FOR LIFE')
