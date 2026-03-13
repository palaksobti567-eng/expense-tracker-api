def error_response(message, details=None):
    return {
        "error": message,
        "details": details
    }
class APIError(Exception):
    """Base class for API Exceptions"""
    def __init__(self, message, details=None):
        self.message=message
        self.details= details
        super().__init__(message)

class InvalidExpenseError(APIError):
    pass
    
class ExpenseNotFoundError(APIError):
    def __init__(self,message="Expense not found",details=None):
        super().__init__(message,details)
class DatabaseError(Exception):
    def __init__(self,message="Database Error",details=None):
        super().__init__(message,details)