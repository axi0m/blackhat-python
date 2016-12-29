# Chapter 2 UDP Client example from Black Hat Python
# Date: 06-28-2016
# Author: axi0m

import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAAABBBBCCCC",(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print data