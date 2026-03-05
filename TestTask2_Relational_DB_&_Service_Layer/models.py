from extentions import db

class User(db.Model):
    """
    User class represents users table in database
    """
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Author(db.Model):
    """
    Author class reprsents authors table in database
    """
    
    __tablename__ = 'authors' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.Column(db.String(500))

    books = db.relationship('Book', backref='author', cascade='all, delete-orphan')
   
    
class Book(db.Model):
    """ 
    Book class represents books table in database
    """
    
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)