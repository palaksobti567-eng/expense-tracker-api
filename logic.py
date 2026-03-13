from db import insert_expense,update_expense,delete_expense
from errors import InvalidExpenseError, ExpenseNotFoundError,DatabaseError
from decimal import Decimal, InvalidOperation,ROUND_HALF_UP


def validate_expense_data(amount,description):
   if isinstance(amount,bool):
      raise InvalidExpenseError("Invalid amount","Boolean not allowed")
   try:
      amount = Decimal(str(amount))
   except (InvalidOperation,ValueError):
      raise InvalidExpenseError("Invalid amount","Must be numeric")
   if amount <= 0:
      raise InvalidExpenseError("Invalid amount","Must be positive")
   amount=amount.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
   if amount > Decimal("1000000"):
      raise InvalidExpenseError("Invalid amount", "Exceed limit")
   if not isinstance(description,str):
      raise InvalidExpenseError("Invalid description", "Must be string")
   description = description.strip()
   if not description:
      raise InvalidExpenseError("Invalid description","Cannot be empty")
   if len(description) >100:
      raise InvalidExpenseError("Invalid description","Too long")
   return amount,description
def validate_expense_id(expense_id):
    if not isinstance(expense_id, int):
        raise InvalidExpenseError("Invalid ID","ID must be an integer")

    if expense_id <= 0:
        raise InvalidExpenseError("Invalid ID","ID must be positive")
    return expense_id
def create_expense(amount, description):
    amount,description = validate_expense_data(amount,description)
    return insert_expense(amount,description)

def update_expense_logic(expense_id,amount,description):
   validate_expense_id(expense_id)

   amount,description = validate_expense_data(amount,description)
   
   rowcount = update_expense(expense_id,amount, description)
   if rowcount == 0:
      raise ExpenseNotFoundError("Expense not found","No record matches ID")
   return rowcount

def delete_expense_logic(expense_id):
   validate_expense_id(expense_id)
   rowcount = delete_expense(expense_id)

   if rowcount == 0:
      raise ExpenseNotFoundError()
   
   return rowcount