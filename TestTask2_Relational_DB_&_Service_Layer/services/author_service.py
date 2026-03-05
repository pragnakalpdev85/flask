from extentions import db
from errors import AppErrors

from models import Author
from models import Book

class AuthorService:
    """
    AuthorService class contains business logic for creating new author, retrieving data of author with books
    and deleting user functionalities.
    """   
     
    @staticmethod
    def create_author(name, bio) -> dict:
        """
        Creates new user and store it in database
        
        Args:
            name (str): name of the author
            bio (str): author bio
        Returns:
            dict: dictionary of author data
        """
        present = Author.query.filter_by(name = name).first()
        
        if present:
            raise AppErrors("Author already exists", 400)
        
        author =  Author(name = name, bio = bio)
        db.session.add(author)
        db.session.commit()
        
        return author
   
    @staticmethod
    def get_author_with_books(id) -> dict:
        """
        Retrieves data of perticular author with all books
        
        Args:
            id (int): id of the author
        Returns:
            dict: dictionary of author data
        """
        author = Author.query.filter_by(id = id).first()
        
        if not author:
            raise AppErrors(f"Author with id {id} does not exists", 400)
        
        books = Book.query.filter_by(author_id = id).all()
        list_books = []
        for book in books:
            list_books.append({
                'id': book.id,
                'title': book.title,
            })
        
        return {'author_id': author.id, "name": author.name, "bio":author.bio, "books": list_books}
    
    @staticmethod
    def delete_author(id) -> dict:
        """
        Deletes author and books associated with author from database
        
        Args:
            id (int): id of the author
        Returns:
            dict: dictionary of author data
        """
        author = Author.query.filter_by(id = id).first()
        
        if not author:
            raise AppErrors(f"Author with id {id} does not exists", 400)
        
        db.session.delete(author)
        db.session.commit()
        
        return author