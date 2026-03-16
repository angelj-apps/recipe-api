from flask import Flask, request, jsonify

app = Flask(__name__)

recipes = {}

@app.route("/")
def home():
    return {"message": "Welcome to the Recipe API"}

@app.route("/recipes/<int:recipe_id>", methods=["POST"])
def add_recipe(recipe_id):
    data = request.get_json()
    # minimal validation
    if "name" not in data or "ingredients" not in data or "cook_time" not in data:
        return jsonify({"error": "Missing fields"}), 400
    recipes[recipe_id] = {
        "name": data["name"],
        "ingredients": data["ingredients"],
        "cook_time": data["cook_time"]
    }
    return jsonify({"message": "Recipe added", "data": recipes[recipe_id]}), 201

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)

@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    if recipe_id in recipes:
        return jsonify(recipes[recipe_id])
    return jsonify({"error": "Recipe not found"}), 404

@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    if recipe_id in recipes:
        del recipes[recipe_id]
        return jsonify({"message": "Recipe deleted"})
    return jsonify({"error": "Recipe not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)