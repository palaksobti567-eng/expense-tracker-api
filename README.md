# Expense Tracker API

## Project Overview

This project is a REST API built with Flask for managing expenses.

It allows users to create, retrieve, and delete expense records while demonstrating key backend concepts such as clean architecture, input validation, error handling, and database persistence using SQLite.

The project follows a layered design to separate HTTP handling, business logic, and database operations.

---

## Features

- Create a new expense
- Retrieve all expenses
- Delete an expense
- Input validation for API requests
- Structured error handling with custom exceptions
- SQLite database persistence
- Layered architecture (routes → services → database)

---

## Tech Stack

- Python
- Flask
- SQLite
- JSON (request/response format)

---

## Project Structure


expense-tracker/
├── app.py # Entry point, initializes Flask app
├── routes.py # Handles HTTP endpoints
├── logic.py # Business logic and validation
├── db.py # Database operations
├── errors.py # Custom exception definitions
├── requirements.txt # Dependencies
└── expense.db # SQLite database


### Architecture

The project follows a layered architecture:

- **routes.py** → Handles HTTP requests and responses  
- **logic.py** → Contains validation and business logic  
- **db.py** → Handles database interactions  
- **errors.py** → Defines custom exceptions  

This separation ensures clean code, easier debugging, and better scalability.

---

## Setup Instructions

1. Clone the repository


git clone https://github.com/palaksobti567-eng/expense-tracker.git


2. Navigate to the project directory


cd expense-tracker


3. Install dependencies


pip install -r requirements.txt


---

## Running the Server

Start the Flask application:


python app.py


The server will run at:


http://127.0.0.1:5000


---

## API Endpoints

### GET /expenses

Returns all stored expenses.

**Response Example:**

```json
[
  {
    "id": 1,
    "amount": 500,
    "description": "Groceries"
  }
]

Status Code: 200 OK

POST /expenses

Creates a new expense.

Request Body:

{
  "amount": 500,
  "description": "Food"
}

Response:

{
  "id": 1,
  "amount": 500,
  "description": "Food"
}

Status Code: 201 Created

DELETE /expenses/<id>

Deletes an expense by ID.

Response:

{
  "message": "Expense deleted successfully"
}

Status Code: 200 OK

Error Handling

The API uses structured error handling with custom exceptions.

Example Errors

Invalid Input (400):

{
  "error": "Invalid amount",
  "details": "Amount must be greater than 0"
}

Not Found (404):

{
  "error": "Expense not found"
}

Server Error (500):

{
  "error": "Internal server error"
}
Error Flow
services.py → raises exception  
routes.py → catches exception → returns HTTP response
Validation Rules

All validation is handled in the service layer.

Rules include:

Amount must be numeric

Amount must be greater than zero

Description must not be empty

This ensures invalid data never reaches the database.

Request Flow
Client
  ↓
routes.py (HTTP handling)
  ↓
services.py (validation + business logic)
  ↓
db.py (database operations)
  ↑
services.py
  ↑
routes.py (response formatting)
  ↓
Client
Testing the API

You can test the API using:

Postman

curl

Example (curl)
curl -X POST http://127.0.0.1:5000/expenses \
-H "Content-Type: application/json" \
-d '{"amount": 500, "description": "Food"}'
Future Improvements

Add update expense endpoint

Implement automated tests

Add authentication

Deploy API (Render / AWS)

Final Notes

This project focuses on writing clean, maintainable backend code rather than just making endpoints work. It demonstrates separation of concerns, validation, and proper error handling — key skills for backend development.