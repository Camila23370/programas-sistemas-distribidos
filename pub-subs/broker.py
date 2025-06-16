import socket
import threading

subscribers = {} # topic --> lista de los sockets de los subscritores
lock = threading.Lock()

def handle_Client(conn, addr):
    try:
        msg_type = conn.recv(1024).decode().strip()
        if msg_type.startwith("PUB:"):
            parts = msg_type[4:].split(":", 1)
            if len(parts) != 2:
                conn.close()
                return
            topic, message = parts
         
            print(f"[>] Publicación en '{topic}':{message}")
            with lock:
                for sub in subscribers.get(topic, []):
                    try:
                        sub.sendall(f"[{topic}] {message}".encode())
                    except:
                        continue
        else:
            conn.sendall(b"Comando no reconocido")
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally:
        conn.close()

def start_broker(hots='0.0.0.0', port=14000)
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[BROKER] Escuchando en {host}:{port}...")
    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_Client, args=(conn, addr),deamon=True).start()
    except KeyboardInterrupt:
        print("Broker detenido")
    finally:
        server.close()
if _name_ == "_main_":
  start_broker()