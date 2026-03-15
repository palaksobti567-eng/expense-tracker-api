Expense Tracker API Documentation
Overview

The Expense Tracker API allows users to create, view, and delete expense records.

The API stores data in a SQLite database and exposes endpoints for managing expenses.

Base URL:

http://127.0.0.1:5000
GET /expenses
Purpose

Retrieve all stored expenses.

This endpoint returns a list of all expense records stored in the database.

Example Request
GET /expenses

Using curl:

curl http://127.0.0.1:5000/expenses
Example Response
200 OK
[
  {
    "id": 1,
    "amount": 200,
    "description": "Food",
    "created_at": "2026-03-14 12:30:10"
  }
]

If no expenses exist:

[]
Status Codes
Code	Meaning
200	Request successful
500	Internal server error
POST /expenses
Purpose

Create a new expense.

This endpoint inserts a new expense record into the database.

Request Body

The request must be sent as JSON.

Example:

{
  "amount": 500,
  "description": "Groceries"
}
Example Request
POST /expenses

Using curl:

curl -X POST http://127.0.0.1:5000/expenses \
-H "Content-Type: application/json" \
-d '{"amount": 500, "description": "Groceries"}'
Example Response
201 Created
{
  "id": 3
}

This indicates the expense was successfully created.

Error Responses

Invalid input:

400 Bad Request

Example:

{
  "error": "Invalid amount",
  "details": "Must be numeric"
}

Unsupported media type:

415 Unsupported Media Type

Example:

{
  "error": "Unsupported Media Type",
  "details": "Content-Type must be application/json"
}

Server error:

500 Internal Server Error
DELETE /expenses/<id>
Purpose

Delete an expense by its ID.

Example Request
DELETE /expenses/3

Using curl:

curl -X DELETE http://127.0.0.1:5000/expenses/3
Example Response
200 OK
{
  "message": "Expense deleted successfully"
}
Error Response

If the expense does not exist:

404 Not Found
{
  "error": "Expense not found"
}
Error Response Format

All API errors follow this structure:

{
  "error": "Error message",
  "details": "Additional information"
}
Technologies Used

Python

Flask

SQLite

How to Run the API

1️⃣ Clone the repository

git clone <your-repo-url>

2️⃣ Install dependencies

pip install flask

3️⃣ Run the application

python app.py

The API will start at:

http://127.0.0.1:5000