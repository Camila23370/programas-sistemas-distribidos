
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
orders = []

USER_SERVICE_URL = "http://user_service:5001/users"
PRODUCT_SERVICE_URL = "http://product_service:5002/products"

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    user_id = data["user_id"]
    product_id = data["product_id"]

    user_res = requests.get(f"{USER_SERVICE_URL}/{user_id}")
    if user_res.status_code != 200:
        return jsonify({"error": "Usuario no encontrado"}), 400

    product_res = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
    if product_res.status_code != 200:
        return jsonify({"error": "Producto no encontrado"}), 400

    order = {
        "user": user_res.json(),
        "product": product_res.json()
    }
    orders.append(order)
    return jsonify(order), 201

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
