#!/usr/bin/env python3

import socket

# Create a TCP/IP socket
#AD_INET: especifica el uso de IPV4 como protocolo de internet que se va a usar.
#SOCK_STREAM: especifica el uso de TCP como protocolo para el tipo del socket que se va a usar.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 52186)
print('starting up on %s port %s', server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen()

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
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
        # Clean up the connection
        connection.close()
