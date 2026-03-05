class AppErrors(Exception):
    """
    AppErrors class for custom error handling
    """
    
    def __init__(self, message: str, status_code=400):
        '''
        Initializes AppError object
        
        Args:
            message (str): error message
            status_code (int): HTTP status code
        '''
        
        super().__init__(message)
        self.message = message
        self.status_code = status_code