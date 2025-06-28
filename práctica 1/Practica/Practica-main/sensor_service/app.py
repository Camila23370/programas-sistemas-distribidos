from flask import Flask, jsonify
import requests
import random
import time
import threading
from datetime import datetime

app = Flask(__name__)
COLLECTOR_URL = "http://collector_service:5002/collector"

barrios = ["roma", "condesa", "del_valle"]
tipos = ["temperatura", "humedad", "calidad_aire"]
INTERVALO = 2 * 60 * 60  # 2 horas en segundos

def enviar_datos_periodicos():
    while True:
        data = { #asigna aleatoriamente cantidades a temperatura, humedad y calidad de aire
            "barrio_id": random.choice(barrios),
            "tipo": random.choice(tipos),
            "valor": round(random.uniform(10, 45), 2),
            "timestamp": datetime.utcnow().isoformat()
        }
        try: #enviar datos:
            requests.post(COLLECTOR_URL, json=data, timeout=5)
            print(f"[{datetime.now()}] Dato enviado:", data)
        except Exception as e:
            print(f"[{datetime.now()}] Error al enviar dato:", e)
        time.sleep(INTERVALO)

@app.route("/sensor/start", methods=["GET"])
def start_sensor():
    thread = threading.Thread(target=enviar_datos_periodicos)
    thread.daemon = True
    thread.start()
    return jsonify({"mensaje": "Sensor programado para emitir datos cada 2 horas"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
