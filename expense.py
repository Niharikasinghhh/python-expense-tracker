
from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        return amount

    except ValueError:
        raise ValueError("Enter a valid positive amount.")


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date

    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")


def get_expense_details():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    date = validate_date(date)

    category = input("Enter category: ").strip()
    if not category:
        raise ValueError("Category cannot be empty.")

    amount = input("Enter amount: ").strip()
    amount = validate_amount(amount)

    description = input("Enter description: ").strip()

    return {
        "date": date,
        "category": category.title(),
        "amount": amount,
        "description": description
    }
