from ..extentions import db

class User(db.Model):
    """
    Represents users model in database
    
    Attributes:
        id (int): id of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
        email (str): email of the user
        password (str): password of the user
        address (str): address of the user
        hobbies (str): hobbies of the user
        gender (bool): user's gender
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String(12), nullable = False)
    address = db.Column(db.String(255), nullable = False)
    hobbies = db.Column(db.String(255), nullable = False)
    gender = db.Column(db.Boolean, nullable = False)