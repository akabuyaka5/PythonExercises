#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 52186)
print('starting up on %s port %s', server_address)
sock.bind(server_address)

sock.listen()

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            print('received "%s"', data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break

    finally:
        connection.close()
