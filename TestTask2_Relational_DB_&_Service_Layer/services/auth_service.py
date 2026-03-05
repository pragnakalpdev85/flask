from flask_jwt_extended import create_access_token
from extentions import bcrypt, db
from errors import AppErrors

from models import User

class AuthService:
    """
    AuthService class contains business logic for user registration and login functionality
    """
    
    @staticmethod
    def register_user(username: str, email: str, password: str) -> dict:
        """
        Registers new user
        
        Args:
            username (string): name o the user
            email (string): email of the user
            password (string): password for user login
        """
        
        if User.query.filter_by(email = email).first() or User.query.filter_by(username = username).first():
            raise AppErrors("User already exists", 400)

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        user = User(username = username, email = email, password = password_hash)
        db.session.add(user)
        db.session.commit()
        
        return user
    
    @staticmethod
    def login_user(email: str, password: str) -> dict:
        """
        Function for user login
        
        Args:
            email (string): email of the user
            password (string): password for user login
        """
        
        user = User.query.filter_by(email = email).first()
        
        if not user or not bcrypt.check_password_hash(user.password, password):
            raise AppErrors("Invalid credentials", 401)
        
        access_token = create_access_token(identity=str(user.id))
        
        return {"access_token": access_token, "user_id": user.id}
