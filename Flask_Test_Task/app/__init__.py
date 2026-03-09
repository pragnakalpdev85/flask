from flask import Flask
from config import Config

from .extentions import db, migrate, jwt, mail
from .models.users import User

from .routes.auth_routes import auth_bp

def create_app(config_class = Config):
    """
    Creates flask application
    
    Returns:
        object: flask applicaion object
    """
    
    #creating flask app
    app = Flask(__name__)
    
    #configuring Config class
    app.config.from_object(config_class)
    
    #loading extenstions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    
    app.register_blueprint(auth_bp)
    
    return app