#--*--coding:UTF-8 --*--

import socket, sys

host = sys.argv[1]
textPort = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textPort)
except ValueError:
    port = socket.getservbyname(textPort, 'udp')

print ("Escribe")
data = sys.stdin.readline().strip()
s.sendall(data)
print("esperando")
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print(buf)