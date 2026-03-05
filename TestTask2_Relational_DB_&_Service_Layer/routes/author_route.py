from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from errors import  AppErrors
from typing import Optional

from services.author_service import AuthorService
from services.user_service import UserService

author_bp = Blueprint('authors', __name__, url_prefix='/authors')

def validate_req_body(req_body: dict) -> Optional[tuple]:
    """
    Helper function that validates req_body data for creating new author
    
    Args:
        req_body (dict): request body with json data of the author
    Returns:
        Optional[tuple]: returns tuple of error message and status code
    """
    if not req_body:
        return ("Request body is required", 400)
    
    if 'name' not in req_body:
        return ("name field is required", 400)
    
    if 'bio' not in req_body:
        return ("bio field is required", 400)
        

def validate_user_login():
    """
    Validated if user is logged in or not
    """
    current_user_id = get_jwt_identity()
    
    user = UserService.get_user_by_id(int(current_user_id))
    if not user:
        return ("Invalid credential", 404)
    
    return None   

@author_bp.route('/', methods=['POST'])
@jwt_required()
def create_new_author():
    """
    This function responds to POST request on author route
    recieves author data and creates new author
    """
    
    islogin = validate_user_login()
    if islogin:
        raise AppErrors(islogin[0], islogin[1])
    
    req_body = request.get_json()
    
    isvalid = validate_req_body(req_body)
    if isvalid:
        raise AppErrors(isvalid[0], isvalid[1])
    
    author = AuthorService.create_author(req_body['name'], req_body['bio'])
    
    return jsonify({"Message": "Author created", "Author": {"name": author.name, "bio": author.bio}}), 201

@author_bp.route('/<id>', methods=['Get'])
@jwt_required()
def get_author_with_books(id):
    """
    This function responds to GET request on author/id route
    and returns user by id
    
    Args:
        id (int): id of the user
    """
    
    current_user_id = get_jwt_identity()
    
    user = UserService.get_user_by_id(int(current_user_id))
    if not user:
        raise AppErrors("Invalid credential", 404)
    
    author = AuthorService.get_author_with_books(id = id)
    
    if not author:
        raise AppErrors('Author not found', 404)
    
    return jsonify({"Message": "Author with all books", "Author": {"name": author['name'], "bio": author['bio'], "Books": author['books']}}), 200

@author_bp.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete_author(id):
    """
    This function responds to DELETE request on author/id route
    and deletes user by id
    
    Args:
        id (int): id of the user
    """
    
    current_user_id = get_jwt_identity()
    
    user = UserService.get_user_by_id(int(current_user_id))
    if not user:
        raise AppErrors("Invalid credential", 404)
    
    author = AuthorService.delete_author(id)
    
    if not author:
        raise AppErrors('Author not found', 404)
    
    return jsonify({"Message": "deleted author", "Author": {"name": author.name, "bio": author.bio}})
    
    