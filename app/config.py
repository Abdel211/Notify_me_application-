import os

class Config:
    """Configuration principale pour l'application."""
    # Configuration Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")  

    # Mail config 
    EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")  # Serveur SMTP par défaut
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))  # Port SMTP
    EMAIL_USE_TLS = bool(int(os.environ.get("EMAIL_USE_TLS", 1)))  
    EMAIL_USER = os.environ.get("EMAIL_USER", "ankasoubaaiabdelmajid@gmail.com")  # mail
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "rtgc mkkj kwvj ktrn")  # pswd
    
    # SMS in case 
    SMS_API_KEY = os.environ.get("SMS_API_KEY", "your_sms_api_key")

# Load confifg 
config = Config()
