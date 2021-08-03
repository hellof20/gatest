# -*- coding: utf-8 -*-

import socket
import time

connect_start = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('76.223.88.101', 30000))
connect_end = time.time()
connect_time = (connect_end-connect_start) * 1000
print('connect time cost : %.2f ms' %connect_time)

#first package
s.send(str('a').encode('utf-8'))
s.recv(1024).decode('utf-8')
first = time.time()
first_time = (first-connect_start)*1000
print('first package time cost : %.2f ms' %first_time)

#second package
s.send(str('a').encode('utf-8'))
s.recv(1024).decode('utf-8')
second = time.time()
second_time = (second - first) * 1000
print('second package time cost : %.2f ms' %second_time)
s.close()
