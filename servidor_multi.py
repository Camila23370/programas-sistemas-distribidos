from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process, Queue
import time
import sys

def worker(task_queue):
    while True:
        if not task_queue.empty():
            conn, addr = task_queue.get()
            print(f"Procesando solicitud de {addr}")
            try:
                data = conn.recv(1024)
                print(f"Mensaje recibido de {addr}: {data.decode()}")
                time.sleep(1)  # Simula procesamiento
                conn.sendall(b"Respuesta del servidor distribuido")
            except Exception as e:
                print(f"Error con cliente {addr}: {e}")
            finally:
                conn.close() 
        else:
            time.sleep(0.1)

def start_server(port, host='localhost', num_workers=3):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escuchando en {host}:{port}")

    task_queue = Queue()

    workers = [Process(target=worker, args=(task_queue,)) for _ in range(num_workers)]
    for w in workers:
        w.start()

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Cliente conectado: {addr}")
            task_queue.put((conn, addr))
    except KeyboardInterrupt:
        print("Servidor detenido manualmente.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python servidor_multi.py <puerto>")
    else:
        try:
            port = int(sys.argv[1])
            start_server(port)
        except ValueError:
            print("Error: El puerto debe ser un número entero.")