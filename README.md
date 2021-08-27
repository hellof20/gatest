# latency_test_for_GA
**latency_test_for_GA** is a set of scripts for testing server and client latency delays, including udp server and udp client. 

After using AWS Global Accelerator, the edge node will quickly return after receiving the tcp and icmp packets, which is not very friendly to the delay test. Therefore, after using AWS Global Accelerator, UDP can be used for delay testing.

## Usage
First, You need to modify the maximum packet size received and sent limit by Linux to 65535 on server and client.
```
$ sudo sysctl -w net.core.rmem_max=65535
```

- Server Setup

  You can pass the port as a parameter to udpserver.py
```
$ python udpserver.py port_num
```

- Configure AWS Global Accelerator to point to the udp server

- Client Setup

  You can pass the server_ip, port_num and packet_size as parameters to udpclient.py
```
$ python udpclient.py server_ip port_num packet_size
```

## Result
```
[ec2-user@ip-192-9-10-51 ~]$ python udpclient.py 13.229.91.162 30000 5
5 bytes send and received
time cost : 146.23 ms
```
