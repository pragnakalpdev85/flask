import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class contains all configuration data for application
    
    Attributes:
        DEBUG (bool): sets debug mode True or False
        SQLALCHEMY_DATABASE_URI (str): uri for database connection
        SQLALCHEMY_TRACK_MODIFICATIONS (str): sets modification tracking mode to true or false
        JWT_SECRET_KEY (str): secret key for jwt authentication
    """
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False