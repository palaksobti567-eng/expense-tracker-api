import sqlite3
from errors import DatabaseError
DB_NAME = "expense.db"

def get_connection():
     return sqlite3.connect(DB_NAME)

def init_db():
      with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                           id INTEGER PRIMARY KEY,
                           amount NUMERIC NOT NULL,
                           description TEXT NOT NULL,
                           created_at TEXT NOT NULL
                           )
                           """)
            cursor.execute("""
                           CREATE INDEX IF NOT EXISTS idx_expenses_created_at
                           ON expenses(created_at)
                           """)

def execute_query(query,params=(),fetch=None):
    """
    Centralized database execution helper.
    fetch options:
    - None      → return cursor (for INSERT/UPDATE/DELETE)
    - "one"     → return single row
    - "all"     → return all rows
    """
    try:
      with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)

        if fetch == "one":
            return cursor.fetchone()

        if fetch == "all":
            return cursor.fetchall()

        conn.commit()
        return cursor
      
    except sqlite3.Error as e:
         print("SQL ERROR:",e)
         
         raise DatabaseError("Database operation failed",str(e))

def insert_expense(amount, description):
        cursor=execute_query(
            """
            INSERT INTO expenses (amount, description, created_at)
            VALUES (?, ?, datetime('now'))
            """,
            (amount, description)
        )
        return cursor.lastrowid
    
def delete_expense(expense_id):
    
        cursor=execute_query(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        )
        return cursor.rowcount
    
def update_expense(expense_id,amount,description):
    
        cursor=execute_query(
            """
            UPDATE expenses
            SET amount =?,description=?
            WHERE id = ?
            """,
            (amount,description,expense_id)
        )

        return cursor.rowcount
    
def get_all_expenses():
    
        return execute_query(
            """
            SELECT id, amount, description , created_at
            FROM expenses
            ORDER BY created_at DESC
            """,
            fetch="all"
        )

        