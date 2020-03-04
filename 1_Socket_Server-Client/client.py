#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 52186

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as msocket:
    msocket.connect((HOST, PORT))
    msocket.sendall(b'BAD BOYS')
    data = msocket.recv(1024)
    print('Received', repr(data))
