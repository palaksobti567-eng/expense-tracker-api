# Expense Tracker API

## Overview

This project is a simple backend API for managing expenses.
It is built to practice backend architecture, error handling, validation, and defensive programming.

The API allows clients to:

* Create an expense
* Delete an expense
* Retrieve expenses

The focus of the project is **clean architecture and clear separation of responsibilities**, not just making the code work.

---

# Architecture

The project follows a **layered architecture** to separate concerns and reduce bugs.

```
project/
 ├── routes.py
 ├── logic.py
 ├── db.py
 └── errors.py
```

### routes.py — HTTP Layer

Responsibilities:

* Receive HTTP requests
* Parse request data (JSON)
* Call business logic
* Convert results into HTTP responses
* Convert exceptions into proper HTTP error responses

Routes should **not contain business rules or SQL logic**.

---

### logic.py — Business Logic Layer

Responsibilities:

* Enforce application rules
* Validate input data
* Maintain invariants

Examples of rules:

* `amount` must be a positive number
* `description` must not be empty
* `id` must be a positive integer

If a rule is violated, the logic layer **raises a domain exception**.

---

### db.py — Database Layer

Responsibilities:

* Handle database connections
* Execute SQL queries
* Return database results

This layer **does not perform validation**.
It only performs persistence operations.

---

### errors.py — Error Definitions

Responsibilities:

* Define custom exception types
* Provide a consistent error response format

Example errors:

* `InvalidExpenseError`
* `ExpenseNotFoundError`
* `DatabaseError`

All errors returned to the client follow the same JSON structure:

```
{
  "error": "Error message",
  "details": "Additional explanation"
}
```

---

# Error Handling Philosophy

Errors are handled using **exception propagation**.

The flow is:

```
logic.py raises exception
      ↓
routes.py catches exception
      ↓
routes.py returns HTTP response
```

This keeps business logic independent from HTTP behavior.

Example:

```
InvalidExpenseError → HTTP 400
ExpenseNotFoundError → HTTP 404
DatabaseError → HTTP 500
```

---

# Validation Approach

All validation happens in **logic.py**.

Reasons:

* Prevent invalid data from reaching the database
* Avoid duplication across multiple routes
* Keep business rules independent from HTTP

Example validations:

* amount must be numeric
* amount must be greater than zero
* description must not be empty

---

# Request Flow

Example request:

```
POST /expenses
{
  "amount": 50,
  "description": "food"
}
```

System flow:

```
Client
  ↓
routes.py (HTTP parsing)
  ↓
logic.py (validation + rules)
  ↓
db.py (SQL execution)
  ↑
logic.py
  ↑
routes.py (format response)
  ↓
Client receives JSON response
```

---

# Example Response

Successful request:

```
{
  "id": 42
}
```

Error response:

```
{
  "error": "Invalid amount",
  "details": "Amount must be positive"
}
```

---

# What This Project Demonstrates

This project focuses on:

* Separation of concerns
* Defensive programming
* Error propagation
* Input validation
* Clean backend architecture
