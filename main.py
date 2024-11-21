from app import create_app
from flask import jsonify

# Créez l'instance de l'application Flask
app = create_app()

@app.route("/", methods=["GET"])

def home():
    return jsonify({"message": "Welcome to the Notification Service. Go to /api/ for the API."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

