#--*-- coding:UTF8 --*--
import socket, sys

host = sys.argv[1]
port = 21

def fin():
    data = s.recv(1024)
    print(data)
    if data == "":
        pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (host, port) )
fin()
s.send("USER anonymous\r\n")
fin()
s.send("PASS anonymous\r\n")
fin()
s.send("HELP\r\n")
fin()
s.send("QUIT\r\n")
s.close()