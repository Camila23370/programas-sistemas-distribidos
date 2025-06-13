# Servidor Web
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12345))
server_socket.listen(1)
print("Esperando conexión ...")

conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

data = conn.recv(1024) # el número de 1024 es el tamaño del buffer, es decir el tamaño del que se dispone 
print("Mensaje recibido:", data.decode())

conn.sendall(b"Hola desde el servidor!")
conn.close()