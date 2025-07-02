from flask import Flask, request, jsonify

app = Flask(__name__) #ceación de instancia en flask 
alertas = [] # lista vacía de alertas para cuando se reciba una 

@app.route("/alert", methods=["POST"])
def recibir_alerta():
    data = request.get_json()
    alertas.append(data) # agrega la alerta a la lista
    print("¡ALERTA RECIBIDA!", data) # imprime ese mensaje y la información
    return jsonify({"mensaje": "Alerta recibida"}), 200

@app.route("/alert", methods=["GET"])
def obtener_alertas():
    return jsonify(alertas) # devuelve todas las alertas almacenadas 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
# la dirección IP "0.0.0.0", puede ser cualquier dirección, permite que otros dispositivos accedas
# la app se ejecuta en el puerto 5004