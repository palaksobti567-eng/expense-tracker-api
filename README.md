# Expense Tracker API

## Overview

A simple REST API built with Flask to manage expenses.

This project demonstrates core backend development concepts including:
- Clean architecture (separation of concerns)
- Input validation
- Structured error handling
- Database interaction using SQLite

The API allows clients to:
- Create an expense
- Retrieve all expenses
- Delete an expense

---

## Tech Stack

- Python
- Flask
- SQLite

---

## Project Structure


expense-tracker/
├── app.py
├── routes.py
├── logic.py
├── db.py
├── errors.py
├── requirements.txt
└── expense.db


### Architecture Overview

The project follows a layered architecture:

- **routes.py** → Handles HTTP requests and responses  
- **services.py** → Contains business logic and validation  
- **db.py** → Handles database operations  
- **errors.py** → Defines custom exceptions  

This separation improves maintainability and prevents mixing concerns.

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

---

### POST /expenses

Creates a new expense.

**Request Body:**

```json
{
  "amount": 50,
  "description": "food"
}
DELETE /expenses/<id>

Deletes an expense by ID.

Example Responses

Success:

{
  "id": 42
}

Error:

{
  "error": "Invalid amount",
  "details": "Amount must be positive"
}
Error Handling

The API uses structured error handling with custom exceptions.

Error flow:

services.py → raises exception  
routes.py → catches exception → returns HTTP response

Common status codes:

400 → Bad Request (invalid input)

404 → Resource not found

500 → Internal server error

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