from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from typing import Optional
from errors import AppErrors

from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

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

@auth_bp.route('/register', methods=['POST'])
def register_user():
    """
    This functikon response to POST request, recieves user data
    and registers new user
    """
    
    data = request.get_json()
    
    isvalid = validate_registration_req_body(data)
    if isvalid:
        raise AppErrors(isvalid[0], isvalid[1])

    user = AuthService.register_user(
        data['username'], data['email'], data['password']
    )
    return jsonify({"message": "User registered"}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    """
    This function Responds to POST request , recieves user data and 
    validates user and login user
    """
    data = request.get_json()
    
    isvalid = validate_login_req_body(data)
    if isvalid:
        raise AppErrors(isvalid[0], isvalid[1])

    result = AuthService.login_user(data['email'], data['password'])
    return jsonify(result), 200