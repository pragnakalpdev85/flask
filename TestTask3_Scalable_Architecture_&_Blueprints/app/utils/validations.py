from typing import Optional
from flask_jwt_extended import get_jwt_identity

from ..services.user_service import UserService
from ..services.author_service import AuthorService

def validate_registration_req_body(req_body: dict) -> Optional[tuple]:
    """
    Helper function that validates req_body data for registration
    
    Args:
        req_body (dict): request body with json data of the user
    Returns:
        Optional[tuple]: returns tuple of error message and status code 
    """
    
    if not req_body:
        return ("Request body is required", 400)
    
    if 'username' not in req_body:
        return ("Username field is required", 400)
    
    if 'email' not in req_body:
        return ("Email field is required", 400)
    
    if 'password' not in req_body:
        return ("password field is required", 400)
    
    return None

def validate_login_req_body(req_body: dict) -> Optional[tuple]:
    """
    Helper function that validates req_body data for login
    
    Args:
        req_body (dict): request body with json data of the user
    Returns:
        Optional[tuple]: returns tuple of error message and status code 
    """
    
    if not req_body:
        return ("Request body is required", 400)
    
    if 'email' not in req_body:
        return ("Email field is required", 400)
    
    if 'password' not in req_body:
        return ("password field is required", 400)
    
    return None

def validate_user_login():
    """
    Validated if user is logged in or not
    """
    current_user_id = get_jwt_identity()
    
    user = UserService.get_user_by_id(int(current_user_id))
    if not user:
        return ("Invalid credential", 404)
    
    return None 

def validate_author_req_body(req_body: dict) -> Optional[tuple]:
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
    
