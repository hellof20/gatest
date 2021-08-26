# -*- coding: utf-8 -*-

import socket
import time
import sys

ip = sys.argv[1]
port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start = time.time()
s.sendto(str('xx').encode('utf-8'), (ip, int(port)))
print(s.recv(102400).decode('utf-8'))
end = time.time()
running_time = (end-start) * 1000
print('time cost : %.2f ms' %running_time)
s.close()
