
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = {"id": user_id, "name": data["name"]}
    return jsonify(users[user_id]), 201

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
