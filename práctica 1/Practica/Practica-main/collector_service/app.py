from flask import Flask, request, jsonify
from flasgger import Swagger
import requests
import logging

app = Flask(__name__)
swagger = Swagger(app)
datos_recolectados = {}

STORAGE_SERVICE_URL = "http://storage_service:5003/storage"
ALERT_SERVICE_URL = "http://alert_service:5004/alert"

logging.basicConfig(level=logging.INFO)

@app.route("/collector/<barrio_id>", methods=["GET"])
def obtener_datos_barrio(barrio_id):
    #buscar el barrio indicado
    if barrio_id not in datos_recolectados or not datos_recolectados[barrio_id]:
        return jsonify({"error": "Barrio no encontrado o sin datos"}), 404

    ultimos_por_tipo = {}

    #buscar los datos de ese barrio
    for dato in datos_recolectados[barrio_id]:
        tipo = dato.get("tipo")
        timestamp = dato.get("timestamp")
        if not tipo or not timestamp:
            continue
        #conseguir el último dato recuperado:
        if tipo not in ultimos_por_tipo or timestamp > ultimos_por_tipo[tipo]["timestamp"]:
            ultimos_por_tipo[tipo] = dato

    #devuelve la lista con los datos:
    return jsonify(list(ultimos_por_tipo.values())), 200

@app.route("/collector", methods=["POST"])
def recibir_dato():
    #conseguir los datos:
    data = request.get_json()
    barrio_id = data.get("barrio_id")
    tipo = data.get("tipo")
    valor = data.get("valor")

    #validar los datos:
    if not all([barrio_id, tipo, valor]):
        return jsonify({"error": "Faltan datos requeridos"}), 400
    if not isinstance(valor, (int, float)):
        return jsonify({"error": "Valor debe ser numérico"}), 400

    datos_recolectados.setdefault(barrio_id, []).append(data)

    #enviar al servicio de almacenamiento:
    try:
        requests.post(STORAGE_SERVICE_URL, json=data, timeout=2)
    except Exception as e:
        logging.error(f"Error al enviar al storage_service: {e}")

    #mensaje de alerta:
    if tipo == "temperatura" and valor > 35:
        alerta = {
            "barrio_id": barrio_id,
            "tipo": tipo,
            "valor": valor,
            "mensaje": "Temperatura crítica"
        }
        try:
            requests.post(ALERT_SERVICE_URL, json=alerta, timeout=2)
        except Exception as e:
            logging.error(f"Error al enviar al alert_service: {e}")

    return jsonify({"mensaje": "Dato recibido y reenviado"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
