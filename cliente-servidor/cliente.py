# Cliente
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creación del socket
client_socket.connect(('localhost',12345))
client_socket.sendall(b"Hola servidor")
respuesta = client_socket.recv(1024)
print("Respuesta del servidor:", respuesta.decode())
client_socket.close()