from ..extentions import db

class Author(db.Model):
    """
    Author class reprsents authors table in database
    """
    
    __tablename__ = 'authors' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.Column(db.String(500))

    books = db.relationship('Book', backref='author', cascade='all, delete-orphan')