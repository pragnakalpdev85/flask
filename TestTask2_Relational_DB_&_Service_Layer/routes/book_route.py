from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from errors import AppErrors
from typing import Optional

from services.book_service import BookService
from services.user_service import UserService
from services.author_service import AuthorService


book_bp = Blueprint('books', __name__, url_prefix='/books')

def validate_book_req_body( req_body: dict) -> Optional[tuple]:
    """
    Helper function that validates req_body data for creating and update books
    
    Args:
        req_body (dict): request body with json data of the author
    Returns:
        Optional[tuple]: returns tuple of error message and status code
    """
    if not req_body:
        return ("Request body is required", 400)
    
    if 'title' not in req_body:
        return ("title field is required", 400)
    
    if 'price' not in req_body:
        return ("price field is required", 400)
    
    if req_body['price'] <= 0:
        return ("Price must be greater than 0", 400)
    
    if 'author_id' not in req_body:
        return ("author_id field is required", 400)
    
    author = AuthorService.get_author_with_books(id= req_body['author_id'])
    if not author:
        return ('Author not found', 404)
        

def validate_user_login():
    """
    Validated if user is logged in or not
    """
    current_user_id = get_jwt_identity()
    
    user = UserService.get_user_by_id(int(current_user_id))
    if not user:
        return ("Invalid credential", 404)
    
    return None  

@book_bp.route('/', methods=['POST'])
@jwt_required()
def create_new_book():
    """
    This function responds to POST request on /books route
    recieves data of the book and store the book in to the database
    """
    islogin = validate_user_login()
    if islogin:
        raise AppErrors(islogin[0], islogin[1])
    
    req_body = request.get_json()
    isvalid = validate_book_req_body(req_body)
    if isvalid:
        raise AppErrors(isvalid[0], isvalid[1])
    
    book = BookService.add_book(title=req_body['title'], price=req_body['price'], author_id=req_body['author_id'])
    
    return jsonify({'message': 'new book is created', 'book':{
        'title': book.title,
        'price': book.price,
        'author_id': book.author_id
    }}), 200
    
@book_bp.route('/<id>', methods=['PUT'])   
@jwt_required() 
def update_book_price(id):
    """
    This function responds to PUT request on /books/<id> route
    recieves book data with updated price and update the price in 
    database
    """
    islogin = validate_user_login()
    if islogin:
        raise AppErrors(islogin[0], islogin[1])
    
    if not BookService.get_book_by_id(id):
        raise AppErrors("Book does not exists", 404)
    
    req_body = request.get_json()
    isvalid = validate_book_req_body(req_body)
    if isvalid:
        raise AppErrors(isvalid[0], isvalid[1])
    
    book = BookService.update_book_price(book_id = id, price = req_body['price'])
    if book.author_id != req_body['author_id']:
        raise AppErrors(f'book is not written by author with id {book.author_id}', 404)
    
    return jsonify({'message': 'book price is updated', 'book':{
        'title': book.title,
        'price': book.price,
        'author_id': book.author_id
    }}), 200   