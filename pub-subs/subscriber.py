import socket
import threading
def listen_to_broker(sock): # función de esucha, se conecta al broker 
    try:
        while True:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
    except:
        print("[!] Conexión cerrada por el broker.")
def main():
    broker_host = 'localhost'
    broker_port = 14000
    topic = input("Tema a suscribirse: ").strip()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((broker_host, broker_port)) # nos conectamos al broker
    sock.sendall(f"SUB: {topic}".encode()) # enviamos el sub y es recibido por el servidor 
    print(f"[SUSCRIPTOR] Suscrito a '{topic}'. Esperando mensaje...")
    threading.Thread(target=listen_to_broker,args=(sock,), daemon=True).start() # se crea un hilo y le pasa la conexion 
    try: 
        while True:
            pass #Mantener activo
    except KeyboardInterrupt:
        print("Saliendo...")
        sock.close()
if __name__ == "__main__":
    main()