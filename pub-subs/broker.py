import socket
import threading

subscribers = {} # topic --> lista de los sockets de los subscritores
lock = threading.Lock() # es un bloqueador "lock"

def handle_client(conn, addr):
    try:
        msg_type = conn.recv(1024).decode().strip()
        if msg_type.startswith("PUB:"):
            parts = msg_type[4:].split(":", 1)  # "4:" quiere decir que a partir de 4 caracteres será lo que se toma en cuenta, es decir que, no tomará en cuenta "PUB:"
            if len(parts) != 2:
                conn.close()
                return
            topic, message = parts # 
            print(f"[>] Publicación en '{topic}':{message}")
            with lock: # ¿qué hace el "whit"? 
                for sub in subscribers.get(topic, []):
                    try:
                        sub.sendall(f"[{topic}] {message}".encode())
                    except:
                        continue
        else:
            conn.sendall(b"Comando no reconocido")
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally: # es opcional, se ejecuta de cualquier manera sin importar si se ejecuto el "try" o el "catch"
        conn.close()

def start_broker(host='localhost', port=14000):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[BROKER] Escuchando en {host}:{port}...")
    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr),deamon=True).start()
    except KeyboardInterrupt:
        print("Broker detenido")
    finally:
        server.close()
if __name__ == "__main__":
  start_broker()