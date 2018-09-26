import socket 
import sys
import math

buf = 1024
direc = ('http://localhost/', 5000)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(direc)
print("servidor activo")

while True:
    peticion, direcclient = serverSocket.recvfrom(buf)
    peticion = peticion.strip() 
    try: 
        resp = "%s" % eval(peticion)
    except:
        resp = "%s" % sys.exc_info()[1]
    serverSocket.sendto("%s" % resp, direcclient)
serverSocket.close()