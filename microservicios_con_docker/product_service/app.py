
from flask import Flask, jsonify

app = Flask(__name__)
products = {
    "1": {"id": "1", "name": "Laptop"},
    "2": {"id": "2", "name": "Teclado"},
    "3": {"id": "3", "name": "Mouse"},
}

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
