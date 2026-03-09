from ..models.users import User
from ..extentions import db

from flask_bcrypt import hashlib
import hmac
import string

class AuthService: 
    """
    AuthService class containes business logic for creating new user and check user presense functionality
    """
    
    @staticmethod
    def create_user(first_name: str, last_name: str, email: str, password: str, address: str, hobbies: list, gender: bool) -> dict:
        """
        Saves new user in the database
        
        Args:
            first_name (str): first name of the user
            last_name (str): last name of the user
            email (str): email of the user
            password (str): password of the user
            address (str): address of the user
            hobbies (str): hobbies of the user
            gender (bool): user's gender
        Returns:
            dict: saved user with success message
        """
        try:
            ispresent = User.query.filter_by(email = email).first()
            
            if ispresent:
                return {'error': "User with same email already exists",'status_code': 400}
            
            password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
            
            user = User(first_name = first_name, last_name = last_name, email = email, password =  password_hash, address = address, hobbies = hobbies, gender = gender)
            db.session.add(user)
            db.session.commit()
            
            return {"message": "user registred successfully", "user": {'first_name': first_name,
                                                            'last_name': last_name, 'email': email,
                                                            'address': address, 'hobbies': hobbies,
                                                            'gender': "male" if gender else "female"}}
        except Exception as e:
            return {'error': "Internal server error"}
    
    @staticmethod  
    def validate_user_password(email: str, password: str) -> dict:
        """
        Checks if user is prsent with matching password.
        
        Args:
            email (str): email of the user
            password (str)
        Returns:
            dict: success message with user id or error message with status code
        """
        try:
            user = User.query.filter_by(email = email).first()
            
            if not user:
                return {'error': "User not found",'status_code': 404}
            
            password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
            
            if not hmac.compare_digest(password_hash, user.password):
                return {'error': 'Wrong password', 'status_code': 400}
            
            
            str_hobbies = ''
            for item in user.hobbies:
                if item.isalpha():
                    str_hobbies += item
                elif item == ',':
                    str_hobbies += ', '
            
            user.hobbies = str_hobbies
            
            user = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'address': user.address,
                'hobbies': user.hobbies,
                'gender': 'male' if user.gender else "female"
            }
            
            return {"message": 'login successful', 'user': user}
        except Exception as e:
            return {'error': "Internal server error"}
    
    @staticmethod
    def updateUser(email: str, first_name: str, last_name: str, address: str, hobbies: list, gender: bool, password: str) -> dict:
        """
        Updates user
        
        Args:
            first_name (str): first name of the user
            last_name (str): last name of the user
            email (str): email of the user
            address (str): address of the user
            hobbies (str): hobbies of the user
            gender (bool): user's gender
        Returns:
            dict: dictionary of user details
        """
        try :     
            user = User.query.filter_by(email = email).first()
            
            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            user.hobbies = hobbies
            user.gender = gender  

            if password:
                user.password = hashlib.md5(password.encode('utf-8')).hexdigest()
            
            db.session.add(user)
            db.session.commit() 
            
            str_hobbies = ''
            for item in user.hobbies:
                if item.isalpha():
                    str_hobbies += item
                elif item == ',':
                    str_hobbies += ', '
            
            user = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'address': user.address,
                'hobbies': str_hobbies,
                'gender': 'male' if user.gender else "female"
            }
            
            return user
        except Exception as e:
            return {'error': "Internal server error"}
    