import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(10):
    s.sendto(str(i), ('', 9999))
    print(s.recvfrom(1024))