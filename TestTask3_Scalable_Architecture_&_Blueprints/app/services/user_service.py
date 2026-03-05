from ..models.user import User

class UserService:
    """
    UserService class contains business logic for get user by id functionality
    """
    
    @staticmethod
    def get_user_by_id(id : int) -> dict:
        """
        Gets user by id from database
        
        Args:
            id (int): id of the user
        Returns:
            dict: dictionary of user found by id
        """
        
        return User.query.filter_by(id = id).first()