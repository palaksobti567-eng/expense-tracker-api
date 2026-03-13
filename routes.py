from errors import error_response,InvalidExpenseError,ExpenseNotFoundError,DatabaseError
import time


@bp.route("/expenses", methods=["POST"])
def create_expense_route():
    start=time.time()
    print("[INFO] Request started: POST /expenses")
    try:
      if not request.is_json:
        raise InvalidExpenseError(
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
      print(f"[INFO] Request failed in {total_duration:.4f} seconds")
        
      total_duration = time.time() - start
      print(f"[INFO] Request failed in{total_duration:.4f} seconds")

      return jsonify({"id" : new_id}), 201
      
    except InvalidExpenseError as e:
       total_duration = time.time() - start
       print(f"[INFO] Validation failed in {total_duration:.4f} seconds")

       return jsonify(error_response(e.message , e.details)), 400
    
    except DatabaseError:
      total_duration = time.time()  - start
      print(f"[INFO] Database error after {total_duration:.4f} seconds")
      return jsonify(error_response(
        "Internal Server Error",
        "Database failure"
    )), 500
    
