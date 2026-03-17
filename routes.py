import time
from errors import error_response,InvalidExpenseError,DatabaseError,ExpenseNotFoundError,UnsupportedMediaTypeError
from logic import create_expense,delete_expense_logic
from flask import request,jsonify
from flask import Blueprint

bp=Blueprint("expenses",__name__)



@bp.route("/expenses", methods=["POST"])
def create_expense_route():
    start=time.time()
    print("[INFO] Request started: POST /expenses")
    try:
      if not request.is_json:
        raise UnsupportedMediaTypeError(
            "Unsupported Media Type",
            "Content-Type must be application/json"
        )

      data = request.get_json()
    
   
      db_start = time.time()
      new_id = create_expense(
            data.get("amount"),
            data.get("description")
        )

      db_duration = time.time() - db_start
      print(f"[INFO] DB operation took {db_duration:.4f} seconds")
        
      total_duration = time.time() - start
      print(f"[INFO] Request completed in {total_duration:.4f} seconds")

      return jsonify({"id" : new_id}), 201
    except UnsupportedMediaTypeError as e:
     return jsonify(error_response(e.message, e.details)), 415   
    except InvalidExpenseError as e:
       total_duration = time.time() - start
       print(f"[INFO] Validation failed in {total_duration:.4f} seconds")

       return jsonify(error_response(e.message , e.details)), 400
    
    except ExpenseNotFoundError as e:
       total_duration = time.time() - start
       print(f"[INFO] Resource not found after {total_duration:.4f} seconds")
       return jsonify(error_response(e.message)),404
     
    except DatabaseError:
      total_duration = time.time()  - start
      print(f"[INFO] Database error after {total_duration:.4f} seconds")
      return jsonify(error_response(
        "Internal Server Error",
        "Database failure"
    )), 500

@bp.route("/expenses/<int:expense_id>",methods=["DELETE"])
def delete_expense_route(expense_id):
   
   start =time.time()
   print(f"[INFO] Request started: DELETE /expense/{expense_id}")

   try:
      
      delete_expense_logic(expense_id)
      total_duration =time.time()  - start
      print(f"[INFO] Delete completed in {total_duration:.4f} seconds")
      
      return jsonify({"message" : "Expense added successfully"})
   
   except InvalidExpenseError as e:
      total_duration = time.time() - start
      print(f"[INFO] Validation failed in{total_duration:.4f} seconds")

      return jsonify(error_response(e.messaege,e.details)),400

   except ExpenseNotFoundError as e:
      total_duration = time.time() - start
      print(f"[INFO] Validation failed in {total_duration:.4f} seconds") 

      return jsonify(error_response(e.message,e.details)), 404
   except DatabaseError:
      total_duration = time.time() - start
      print(f"[INFO] Database error after {total_duration:.4f} seconds") 

      return jsonify(error_response(
         "Internal Server Error",
         "Database failure"
      )),500

    
