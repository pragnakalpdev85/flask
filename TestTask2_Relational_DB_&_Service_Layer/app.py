from config import Config
from flask import Flask, jsonify
from errors import AppErrors
from extentions import db, migrate, jwt

from routes.auth_route import auth_bp
from routes.author_route import author_bp
from routes.book_route import book_bp
    
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

if __name__ == "__main__":
    app = create_app()
    app.run()