import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET -> usar ipv4
# socket.SOCK_STREAM -> para TCP
# socket.SOCK_DGRAM -> para UDP

s.connect( ('www.ediciones-eni.com', 80) ) # Tupla con direccion y puerto

s.send( 'GET /index.html HTML/1.1\r\n\r\n')
data = s.recv(2048) # 2048 bytes
# s.send() -> TCP
# s.sendto() -> UDP
# s.recv() -> TCP
# s.recvfrom() -> UDP
print(data)
s.close()

#while 1:
#   data = s.recv(128)
#   print(data)
#   if data == "":
#       break
#s.close()

