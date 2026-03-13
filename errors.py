def error_response(message, details=None):
    return {
        "error": message,
        "details": details
    }
class InvalidExpenseError(Exception):
    def __init__(self, message, details=None):
        self.message=message
        self.details= details
        super().__init__(message)
    
class ExpenseNotFoundError(Exception):
    def __init__(self,message="Expense not found",details=None):
        self.maessag=message
        self.details=details
        super().__init__(message)
class DatabaseError(Exception):
    def __init__(self,message="Database Error",details=None):
        self.messsage=message
        self.details=details
        super().__init__(message)