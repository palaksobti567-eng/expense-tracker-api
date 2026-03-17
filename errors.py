def error_response(message, details=None):
    return {
        "error": message,
        "details": details
    }
class APIError(Exception):
    """Base class for API Exceptions"""
    status_code = 400
    def __init__(self, message, details=None):
        self.message=message
        self.details= details
        super().__init__(message)
class UnsupportedMediaTypeError(APIError):
    statu_code=415
class InvalidExpenseError(APIError):
    status_code = 400
    
class ExpenseNotFoundError(APIError):
    status_code = 404
    def __init__(self,message="Expense not found",details=None):
        super().__init__(message,details)
class DatabaseError(Exception):
    status_code = 500
    def __init__(self,message="Database Error",details=None):
        super().__init__(message,details)