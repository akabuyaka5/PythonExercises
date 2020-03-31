import html
import socket
from html.parser import HTMLParser

from Requests import requests

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
        print('\n')
        data = connection.recv(1024)
        print('RECEIVED:', data.decode())
        request = requests(data.decode())
        urlRequest = request['URL']
        if urlRequest.__contains__("form"):
            html_content = open('html%s' % urlRequest)
            h = html.parser
            form = html_content.read()
            message = h.unescape(form)
            length = len(message)
            string = "HTTP/1.1 200 OK\r\nCache-Control: no-store\r\nContent-Length: %d\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n%s" % (
                length, message)
        elif urlRequest.__contains__("register"):
            sendall = True

        if data:
            print('Sending data back to the client')
            connection.sendall(string.encode())
        else:
            print('No more data from', client_address)
            break

    finally:
        connection.close()
