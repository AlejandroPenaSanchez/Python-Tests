#--*-- coding:UTF8 --*--
import socket, sys

host = sys.argv[1]
port = sys.argv[2]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as ex:
    print("error en la creacion del socket: %s" % ex)
    sys.exit(1)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Level:
# socket.SOL_SOCKET -> trabajamo con los sockets
# OptName:
# SO_DONTROUTE -> prohibe los paquetes pasar a traves de los routers y las pasarelas
# SO_KEEPALIVE -> permite la trasnmision de paquetes"keepAlive" estos paquetes permiten saber a los nodos si la conexion sigue activa cuando en esta no se pasan datos
# SO_BROADCAST -> permite la transmision y recepcion de paquetes broadcast 
# SO_REUSEADDR -> el puerto utilizado puede reutilizarse de inmediato despues de que el socket se cierra
#hay mucho mas....
s.bind( (host, port) )
s.listen(5)# el numero es el numero maximo de conexiones aceptadas en la cola de recepcion 

client, direction = s.accept()
print(direction)
print("Se ha efectuado una conexino desde ")
print(client.getpeername)
client.close()
s.close()