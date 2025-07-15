# TransactionApp

A simple Flask web application to perform **CRUD (Create, Read, Update, Delete)** operations on a list of financial transactions.

---

Features

- View all transactions
- Add a new transaction
- Edit an existing transaction
- Delete a transaction

---

## Sample Data

The app starts with a predefined list of transactions:

```python
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
````

---

## Project Structure

```
TransactionApp/
├── app.py                 # Main Flask application
├── templates/
│   ├── transactions.html  # Transaction list view
│   ├── form.html          # Add transaction form
│   └── edit.html          # Edit transaction form
└── README.md              # This file
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/transaction-app.git
cd transaction-app
```

### 2. Install dependencies

> This app only requires Flask.

```bash
pip install Flask
```

### 3. Run the application

```bash
python app.py
```

The app will be available at:
(http://localhost:9001](http://localhost:9001)

---

## Routes Overview

| Route                          | Method(s) | Description                  |
| ------------------------------ | --------- | ---------------------------- |
| `/`                            | GET       | View all transactions        |
| `/add_transaction`             | GET, POST | Add a new transaction        |
| `/edit/<int:transaction_id>`   | GET, POST | Edit an existing transaction |
| `/delete/<int:transaction_id>` | POST      | Delete a transaction         |

---

## Notes

* All data is stored **in-memory**, meaning it will reset when the server restarts.
* For production use, consider connecting to a **database** (e.g., SQLite, PostgreSQL).

---

## License

MIT License – use it freely for personal or commercial projects.

```


