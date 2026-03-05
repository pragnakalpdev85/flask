from ..extentions import db

class Book(db.Model):
    """ 
    Book class represents books table in database
    """
    
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)