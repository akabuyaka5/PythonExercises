#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 52186)
print('connecting to %s port %s', server_address)
sock.connect(server_address)

try:
    message = b'This is the message.  It will be repeated.'
    print(b'sending "%s"', message)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"', data)

finally:
    print('closing socket')
    sock.close()
