from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from ..utils.error import AppErrors
from ..utils.validations import validate_user_login, validate_book_req_body

from ..services.book_service import BookService

#blueprint for books routes
book_bp = Blueprint('books', __name__, url_prefix='/api/v1/books')

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
def update_book_price(id: int):
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