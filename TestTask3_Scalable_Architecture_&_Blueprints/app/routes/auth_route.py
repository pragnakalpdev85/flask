from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService

from ..utils.error import AppErrors
from ..utils.validations import validate_login_req_body, validate_registration_req_body

#blueprint for auth routes
auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

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