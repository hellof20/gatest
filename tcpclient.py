# -*- coding: utf-8 -*-

import socket
import time
import sys
import os

ip = sys.argv[1]
port = sys.argv[2]
packet_size = sys.argv[3]

command = "dd if=/dev/urandom of=test bs=" + str(packet_size) + "k count=1"
print(command)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
os.system(command)
f = open("./test", "r")
data=f.read()

connect_start = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))
connect_end = time.time()
connect_time = (connect_end-connect_start) * 1000
print('connect time cost : %.2f ms' %connect_time)

#first package
s.send(data)
s.recv(1024000)
first = time.time()
first_time = (first-connect_start)*1000
print('first package time cost : %.2f ms' %first_time)

#second package
s.send(data)
s.recv(1024000)
second = time.time()
second_time = (second - first) * 1000
print('second package time cost : %.2f ms' %second_time)
s.close()
