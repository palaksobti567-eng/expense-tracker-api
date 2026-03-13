import sqlite3

DB_NAME = "expense.db"
def init_db():
      with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                           id INTEGER PRIMARY KEY,
                           amount REAL,
                           description TEXT,
                           created_at TEXT
                           )
                           """)
            cursor.execute("""
                           CREATE INDEX IF NOT EXISTS idx_expenses_created_at
                           ON expenses(created_at)
                           """)
def execute_query(query,params=(),fetchone=False,fetchall=False):
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(query,params)
        if fetchone:
            return cursor.fetchone()
        if fetchall:
            return cursor.fetchall()
        
        conn.commit()
        return cursor

def get_connection():
      conn = sqlite3.connect(DB_NAME,timeout=5)
      conn.row_factory = sqlite3.Row
      return conn


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
            fetchall=True
        )

        