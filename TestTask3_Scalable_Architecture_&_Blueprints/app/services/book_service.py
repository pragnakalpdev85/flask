from ..models.book import Book
from ..extentions import db

class BookService:
    """
    BookService class contains business logic for creating new book and updating price of 
    book functionalities.
    """   
    
    @staticmethod
    def get_book_by_id(id: int) -> dict:
        """
        Retrieves book from database by id
        
        Args:
            id (int): id of the book
        Returns:
            dict: dictionary of book data
        """
        book = Book.query.filter_by(id = id).first()
        
        return book
    
    @staticmethod
    def add_book(title: str, price: float, author_id: int) -> dict:
        """
        Adds new book with author id into the database
        
        Args:
            title (str): title of the book
            price (float): price of the book
            author_id (int): id of the author who wrote book
        Returns:
            dict: returns dictionary with book data
        """
        
        book = Book(title = title, price = price, author_id = author_id)
        db.session.add(book)
        db.session.commit()
        
        return book
    
    @staticmethod
    def update_book_price(book_id: int, price: float) -> dict:
        """
        Updates books price in database
        
        Args:
            book_id (int): id of the book
            price (float): price of the book
        Returns:
            dict: updated book details
        """
        
        book = Book.query.filter_by(id = book_id).first()
        book.price = price
        
        db.session.add(book)
        db.session.commit()
        
        return book
        