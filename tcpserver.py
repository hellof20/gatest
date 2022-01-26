#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket
import threading
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '0.0.0.0'
server_port = int(sys.argv[1])

server = (server_address, server_port)
s.bind(server)
s.listen(5)
print("Listening on " + server_address + ":" + str(server_port))

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    #sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024000)
        sock.send(data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
