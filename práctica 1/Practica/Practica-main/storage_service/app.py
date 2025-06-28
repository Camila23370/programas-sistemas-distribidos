from flask import Flask, request, jsonify

app = Flask(__name__)
datos_almacenados = {}

@app.route("/storage", methods=["POST"])
#función para guardar la información
def guardar():
    data = request.get_json()
    barrio_id = data.get("barrio_id")

    if not barrio_id: #si no se pudo conseguir el barrio_id
        return jsonify({"error": "Datos inválidos"}), 400

    datos_almacenados.setdefault(barrio_id, []).append(data) #guardar los datos
    return jsonify({"mensaje": "Dato almacenado"}), 201

@app.route("/storage", methods=["GET"])
def obtener_todo():
    return jsonify(datos_almacenados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
