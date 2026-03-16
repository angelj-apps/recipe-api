from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

recipes = {}
next_id = 1

@app.route("/")
def index():
    return send_from_directory("", "index.html")  # serves your HTML page

@app.route("/recipes", methods=["POST"])
def add_recipe():
    global next_id
    data = request.get_json()
    if not data or "name" not in data or "ingredients" not in data or "cook_time" not in data:
        return jsonify({"error": "Missing fields"}), 400
    recipe = {
        "id": next_id,
        "name": data["name"],
        "ingredients": data["ingredients"],
        "cook_time": data["cook_time"]
    }
    recipes[next_id] = recipe
    next_id += 1
    return jsonify({"message": "Recipe added", "data": recipe})

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)