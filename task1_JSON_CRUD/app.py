from flask import request, Flask, jsonify
import json
import uuid
from typing import Optional

app = Flask(__name__)

file_name = 'users.json'


def validate_user_data(data: dict) -> Optional[str]:
    """
    validate user data. 
    
    Args:
        data (dict): dictionary of user data
    Returns:
        str: error message or None.
    """
    
    if not data:
        return "Request body is required"

    if 'name' not in data:
        return "Missing 'name' field"

    if 'email' not in data:
        return "Missing 'email' field"

    if 'age' in data and not isinstance(data['age'], int):
        return "Age must be an integer"

    return None

def validate_data_for_update(data: dict) -> Optional[str]:
    '''
    Validated data given for update
    
    Args:
        data (dict): dictionary of user data
    Returns:
        str: error message or None
    '''
    if not data:
        return "Request body is required"
    
    if ('name' not in data) and ('email' not in data) and ('age' not in data):
        return "Any one field from name or email or age is rquired to update user"
    
    if not isinstance(data['age'], int):
        return "Invalid age"
    
def validate_uuid(user_id: str) -> Optional[str]:
    '''
    validated uuid formate
    
    Args:
        user_id (str): id of the user
    Returns:
        str: error message if error occurs else none
    '''
    
    try:
        uuid.UUID(user_id)
    except ValueError:
        return "Invalid UUID format"
    
    return None
  
    
@app.route('/users', methods=["GET"])
def get_all_users():
    '''
    Retrieves data of all users
    
    Returns:
        tuple: tuple of
            response (flask.Response): JSON object with users data or error message:
            status_code (int): HTTP status code.
         
    '''
    
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)
            
        if not user_data:
            return jsonify({"error": "File is empty"}), 404
            
        return jsonify(user_data), 200
    
    except FileNotFoundError as err:
        return jsonify({'error': "File not found"}), 404
    except json.decoder.JSONDecodeError as e:
        return jsonify({"error": "File is empty"}), 400
 
        
@app.route('/users/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    '''
    Retrieves user with user id
    
    Args:
        user_id (query parameter): id of the user
    Returns: 
        tuple: tuple of
            response (flask.Response): JSON object with user data or error message:
            status_code (int): HTTP status code.
    '''
    
    error_id = validate_uuid(user_id)
    
    if error_id:
        return jsonify({"error": error_id}), 400
    
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)            
        
    except FileNotFoundError as err:
        return jsonify({"error": "File not found"}), 404
    except json.decoder.JSONDecodeError as e:
        return jsonify({"error": "File is empty"}), 400
    
    for user in user_data['users']:
        if user['id'] == user_id:
            return jsonify(user), 200
        
    return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def create_new_user():
    '''
    Creates new user
    
    Expected Request Body:
        data of the user with name, age and eamil
    Returns: 
        tuple: tuple of
            response (flask.Response): JSON object with created user data or error message:
            status_code (int): HTTP status code.
    '''
    data = request.get_json()
    
    error = validate_user_data(data)
    
    if error:
        return jsonify({"error": error}), 400
    
    new_user = {
        'id' : str(uuid.uuid4()),
        'name' : data['name'],
        'email' : data['email'],
        'age' : data['age']
    }
    
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)
            
            data = user_data['users']
            data.append(new_user)
        
        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)
            
            
        return jsonify({"message": "New User is created", "user": new_user}), 201
            
    except FileNotFoundError as err:
        return jsonify({"error": "File not found"}), 404
    except json.decoder.JSONDecodeError as e:
        return jsonify({"error": "File is empty"}), 404

    
@app.route("/users/<user_id>", methods=['PATCH'])
def update_user(user_id):
    '''
    Updates user data
    
    Expected Request Body:
        data of the user with any data from name, age and eamil
    Args:
        user_id (query parameter): id of the user
    Returns: 
        tuple: tuple of
            response (flask.Response): JSON object with updated user data or error message:
            status_code (int): HTTP status code.
    '''
    data = request.get_json()
    
    error = validate_data_for_update(data)
    if error:
        return jsonify({"error": error}), 400
    
    error_id = validate_uuid(user_id)
    if error_id:
        return jsonify({"error": error_id}), 400
    
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)  
        
        updated_user = {}
        found = False
        for user in user_data['users']:
            if user['id'] == user_id:  
                found = True
                user['name'] = data['name'] if 'name' in data else user['name']
                user['email'] = data['email'] if 'email' in data else user['email']
                user['age'] = data['age'] if 'age' in data else user['age']
                updated_user = user
                break
        
        if not found:
            return jsonify({"error": "User not found"}), 404
        
        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)
            
        return jsonify({"message": "User Updated successfully", "user": updated_user}), 200
        
    except FileNotFoundError as err:
        return jsonify({"error": "File not found"}), 404
    except json.decoder.JSONDecodeError as e:
        return jsonify({"error": "File is empty"}), 404
 
    
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    '''
    Deletes User
        
    Args:
        user_id (query parameter): id of the user
    Returns: 
        tuple: tuple of
            response (flask.Response): JSON object with deleted user data or error message:
            status_code (int): HTTP status code.
    '''
    error = validate_uuid(user_id)
    
    if error:
        return jsonify({"error": error}), 400
    
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)  
            
        index = 0
        found = False
        deleted_user = {}
        
        list_users = user_data['users']

        for user in user_data['users']:
            if user['id'] == user_id:
                found = True
                deleted_user = user
                list_users.pop(index)
                break
        
            index += 1
            
        if not found:
            return jsonify({"error": "User not found"}), 404
        
        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)
        
        return jsonify({"message": "User deleted successfully", "user": deleted_user}), 200         
        
    except FileNotFoundError as err:
        return jsonify({"error": "File not found"}), 404
    except json.decoder.JSONDecodeError as e:
        return jsonify({"error": "File is empty"}), 404    


if __name__ == '__main__':
    app.run(debug=True)