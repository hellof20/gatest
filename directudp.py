# -*- coding: utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in range(0,10):    
    start = time.time()
    s.sendto(str(data).encode('utf-8'), ('54.64.75.187', 31337))
    print(s.recv(1024).decode('utf-8'))
    end = time.time()
    running_time = (end-start) * 1000
    print('time cost : %.2f ms' %running_time)
s.close()
