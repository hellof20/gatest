# -*- coding: utf-8 -*-

import socket
import time
import sys
import os

ip = sys.argv[1]
port = sys.argv[2]
packet_size = int(sys.argv[3])
command = "dd if=/dev/urandom of=test bs=" + str(packet_size) + " count=1 > /dev/null 2>&1 &"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
os.system(command)

f = open("./test", "r")
data=f.read()

start = time.time()
s.sendto(data, (ip, int(port)))
print(str(len(s.recv(1024000))) + " bytes ve been sent and received")
end = time.time()
running_time = (end-start) * 1000
print('time cost : %.2f ms' %running_time)
s.close()
