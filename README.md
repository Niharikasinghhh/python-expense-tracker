# Personal Expense Tracker

A command-line Personal Expense Tracker developed using Python. The application helps users record, manage, search, and summarize their daily expenses, with CSV-based storage and input validation.

## Features

- Add new expenses with date, category, amount, and description
- View all recorded expenses
- Search expenses by category
- Edit existing expense records
- Delete expenses using their IDs
- Calculate total spending
- Generate category-wise spending summaries
- Validate dates and amounts
- Handle invalid inputs and file errors
- Store records in a CSV file

## Technologies Used

- Python 3
- CSV
- datetime
- os
- VS Code
- Git and GitHub

## Python Concepts Demonstrated

- Functions and modular programming
- File handling
- CSV reading and writing
- Exception handling (`try`, `except`, `raise`)
- Input validation
- Lists and dictionaries
- Loops and conditional statements
- Basic CRUD operations
- Date validation
- Code organization using modules

## Project Structure

```text
python-expense-tracker/
│
├── main.py
├── expense.py
├── storage.py
├── reports.py
├── expenses.csv
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9 or later
- No external Python libraries required

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/python-expense-tracker.git
   ```

2. Navigate to the project folder:

   ```bash
   cd python-expense-tracker
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Data Storage

Expenses are stored locally in `expenses.csv`.

Each record contains:

- ID
- Date
- Category
- Amount
- Description

Example:

```csv
id,date,category,amount,description
1,2026-10-03,Food,250.0,Lunch
2,2026-10-03,Travel,120.0,Metro
```

## Purpose

This project was developed to strengthen Python programming fundamentals and practice building a structured command-line application with data persistence, input validation, and exception handling.

## Future Improvements

- Monthly spending reports
- Budget limits and alerts
- Export summaries
- Unit tests
- A graphical user interface

## Author

Niharika Singh