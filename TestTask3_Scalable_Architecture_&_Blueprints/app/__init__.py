from flask import Flask, jsonify
from config import Config
from .extentions import db, ma, migrate, jwt
from app.utils.error import AppErrors

from .routes.auth_route import auth_bp
from .routes.author_route import author_bp
from .routes.book_route import book_bp

from app.models.user import User
from app.models.author import Author
from app.models.book import Book

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
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    #registering blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(book_bp)
    
    
    #creating custom error handler
    @app.errorhandler(AppErrors)
    def handle_app_error(e):
        return jsonify({
            "error": e.message,
            "code": e.status_code
        }), e.status_code

    return app