import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))
while 1:
    data, addr = s.recvfrom(8096)
    s.sendto(data, addr)
