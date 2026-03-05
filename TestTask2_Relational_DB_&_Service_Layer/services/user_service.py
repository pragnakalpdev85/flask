from extentions import db
from models import User

class UserService:
    """
    UserService class contains business logic for get user by id functionality
    """
    
    @staticmethod
    def get_user_by_id(id) -> dict:
        """
        Gets user by id from database
        
        Args:
            id (int): id of the user
        Returns:
            dict: object of user found by id
        """
        
        return User.query.filter_by(id = id).first()