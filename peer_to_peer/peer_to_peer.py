import socket 
import threading # ejecuta varias tareas al mismo tiempo
import sys
import time # relacionado al tiempo

# Función para manejar conexiones entrantes
def handle_peer(conn, addr):
    try:
        print(f"[+] Conectado desde {addr}")
        data = conn.recv(1024).decode()
        print(f"[{addr}] → {data}")
        conn.sendall(f"Echo desde {conn.getsockname()}".encode())
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally:
        conn.close()

# Servidor que escucha conexiones entrantes
def peer_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[SERVIDOR] Nodo escuchando en puerto {port}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_peer, args=(conn, addr))
        thread.start()

# Cliente que envía mensajes a otros peers
def connect_to_peers(peers, message):
    for host, port in peers:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                sock.sendall(message.encode())
                response = sock.recv(1024).decode()
                print(f"[{host}:{port}] ⇐ {response}")
        except Exception as e:
            print(f"[!] No se pudo conectar a {host}:{port} - {e}")
#-----------TAREA: EXPANDIR EL CÓDIGO PARA ARCHIVOS TXT------------#
# Función para poder leer el archivo .txt
def leer_archivo(ruta):
    try: 
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e: # en caso de que no se pueda leer
        print(f"[!] Error al leer archivo: {e}")
        return None
# utf-8 es para la decodificación de los caracteres y que puedan ser leidos 

# Programa principal
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python peer_node.py <mi_puerto> <peer1_host:port> [<peer2_host:port> ...]")
        sys.exit(1)

    my_port = int(sys.argv[1])
    peers = [tuple(p.split(":")) for p in sys.argv[2:]]
    peers = [(h, int(p)) for h, p in peers if int(p) != my_port]

    # Iniciar el hilo del servidor
    threading.Thread(target=peer_server, args=(my_port,), daemon=True).start()

    # Dar tiempo a que el servidor escuche
    time.sleep(1)

    print("Acciones:")
    print(" 1. Mensaje")
    print(" 2.'@file:archivo.txt' para enviar un archivo")
    print(" 3. 'exit' ")

    # Enviar mensaje a los peers conocidos
    while True:
        mensaje = input("\nMensaje a enviar (o '@file:archivo.txt' o 'exit'): ")
        
        if mensaje.lower() == 'exit':
            print("[INFO] Saliendo...")
            break
        
        # si es un archivo
        if mensaje.startswith("@file:"):
            ruta = mensaje[6:]  # quita el @file: para que solo se lea el nombre del archivo, son 6 caracteres
            print(f"[INFO] leyendo archivo: {ruta}")
            contenido = leer_archivo(ruta)
            if contenido is not None:
                mensaje = f"[ARCHIVO: {ruta}]\n{contenido}"
                print(f"Archivo leído")
            else:
                print("No se pudo leer el archivo.")
                continue
        
        # envio de mensaje
        print(f"Enviando mensaje a {len(peers)} peer(s)...")
        connect_to_peers(peers, mensaje)