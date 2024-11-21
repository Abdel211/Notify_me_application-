from flask import Blueprint, request, jsonify
from app.config import config
import smtplib
from email.mime.text import MIMEText

# Création d'un Blueprint pour les routes liées aux emails
email_routes = Blueprint("email_routes", __name__)

@email_routes.route("/", methods=["GET"])
def root():
    return jsonify({"message": "API is running!"}), 200

# Route pour envoyer un email
@email_routes.route("/send-email", methods=["POST"])
def send_email():
    try:
        data = request.get_json()
        recipient = data.get("recipient")
        subject = data.get("subject")
        body = data.get("body")
        
        if not all([recipient, subject, body]):
            return jsonify({"error": "All fields (recipient, subject, body) are required"}), 400
        
        # Configuration de l'email
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = config.EMAIL_USER
        message["To"] = recipient

        # Envoi de l'email
        with smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
            server.send_message(message)
        
        return jsonify({"message": f"Email sent to {recipient}!"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
