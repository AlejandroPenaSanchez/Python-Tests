#--*-- coding:UTF8 --*--
import socket, sys

host = sys.argv[1]
port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (host, port) )
s.listen(1)
client, direction = s.accept()
print(direction)
print(client.getpeername())

client.send("Hola Cliente\n introduzca una palabra o fin si desea terminar la conversacion")
while 1:
    data = client.recv(1024)
    if data == "fin\n":
        break
    print("cliente > " + data)
    palabra = input("Servidor > ")
    client.send(palabra)

client.close()
s.close()