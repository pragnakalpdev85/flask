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
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
class DevConfig(Config):
    """
    Configuration class contains all configuration data for devlopement environment
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URI')
    DEBUG = True

class TestConfig(Config):
    """
    Configuration class contains all configuration data for testing environment
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URI')
    DEBUG = False