#--*-- coding:UTF8 --*--
import socket, sys

host = sys.argv[1]
textPort = sys.argv[2]
archivo = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as ex:
    print("error en la creacion del socket: %s" % ex)
    sys.exit(1)

try:
    port = int(textPort)
except ValueError:
    try:
        port = socket.getservbyname(host, 'tcp')
    except socket.error as ex:
        print("no se encuentra el puerto: %s" % ex)
        sys.exit(1)

try:
    s.connect( (host, port) )
except socket.gaierror as ex:
    print("Error de la direccion de conexion al servidor: %s" % ex)
    sys.exit(1)
except socket.error as ex:
    print("Error de conexion: %s" % ex)
    sys.exit(1)

try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % archivo)
except socket.error as ex:
    print("Error en envio de datos:  %s" % ex)
    sys.exit(1)

while True:
    try: 
        buf = s.recv(2048)
    except socket.error as ex:
        print("Error de recepcion de datos: %s" % ex)
        sys.exit(1)
    if not len(buf):
        break
    print(buf)