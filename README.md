# latency_test_for_GA
**latency_test_for_GA** is a set of scripts for testing server and client latency delays, including udp server and udp client. 

After using AWS Global Accelerator, the edge node will quickly return after receiving the tcp and icmp packets, which is not very friendly to the delay test. Therefore, after using AWS Global Accelerator, UDP can be used for delay testing.

## Usage
- server setup
```
$ sudo sysctl -w net.core.rmem_max=65535
$ python udpserver.py 30000
```

- client setup
```
$ sudo sysctl -w net.core.rmem_max=65535
$ python udpclient.py serverip 30000 packetsize
```
