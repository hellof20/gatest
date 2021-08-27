#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = int(sys.argv[1])
packet_size = int(sys.argv[2])
print(packet_size)
command = "dd if=/dev/urandom of=test bs=" + str(packet_size) + "KB count=1"
print(command)
os.system(command)

f = open("./test", "r")
data=f.read()

server = (server_address, server_port)
sock.bind(server)

print("Listening on " + server_address + ":" + str(server_port))
while True:
    payload, client_address = sock.recvfrom(102400)
    print("Echoing data back to " + str(client_address))
    sent = sock.sendto(data, client_address)
