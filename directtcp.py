# -*- coding: utf-8 -*-

import socket
import time

connect_start = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('54.169.74.196', 30000))
connect_end = time.time()
connect_time = (connect_end-connect_start) * 1000
print(s.recv(1024).decode('utf-8'))
print('connect time cost : %.2f ms' %connect_time)

for data in range(0,10):
    start = time.time()
    s.send(str(data).encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
    end = time.time()
    running_time = (end-start) * 1000
    print('running time cost : %.2f ms' %running_time)
s.close()
