from flask import Flask, request, jsonify

app = Flask(__name__)
alertas = []

@app.route("/alert", methods=["POST"])
def recibir_alerta():
    data = request.get_json()
    alertas.append(data)
    print("¡ALERTA RECIBIDA!", data)
    return jsonify({"mensaje": "Alerta recibida"}), 200

@app.route("/alert", methods=["GET"])
def obtener_alertas():
    return jsonify(alertas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
