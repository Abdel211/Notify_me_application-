from flask import Flask
from app.config import config
from app.routes.email_routes import email_routes

def create_app():
    # Initialisez l'application Flask
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_object(config)

    # Enregistrez les blueprints
    app.register_blueprint(email_routes, url_prefix="/api")

    return app
