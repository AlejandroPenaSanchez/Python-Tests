import socket
import sys

buf = 1024
direc = ('localhost',20000)# direccion ip del servidor, puerto

if __name__ == '__main__':
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        peticion = input('?: ').strip()
        if peticion == "":
            break
        mySocket.sendto("%s" % peticion, direc)
        resp, adr = mySocket.recvfrom(buf)
        print("=> %s" % resp)
    mySocket.close()
    print("Fin del cliente UDP")