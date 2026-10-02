
import csv
import os

FILE_NAME = "expenses.csv"

FIELDS = ["id", "date", "category", "amount", "description"]


def initialize_file():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_expenses():
    initialize_file()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except (OSError, csv.Error) as error:
        print("Error reading expenses:", error)
        return []


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(expenses)
        return True

    except (OSError, csv.Error) as error:
        print("Error saving expenses:", error)
        return False


def add_expense(expense):
    expenses = load_expenses()

    if expenses:
        new_id = max(int(item["id"]) for item in expenses) + 1
    else:
        new_id = 1

    expense["id"] = str(new_id)
    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")
        return True

    return False


def delete_expense(expense_id):
    expenses = load_expenses()
    updated = [
        item for item in expenses
        if item["id"] != expense_id
    ]

    if len(updated) == len(expenses):
        print("Expense ID not found.")
        return False

    if save_expenses(updated):
        print("Expense deleted successfully!")
        return True

    return False


def update_expense(expense_id, new_details):
    expenses = load_expenses()

    for item in expenses:
        if item["id"] == expense_id:
            item["date"] = new_details["date"]
            item["category"] = new_details["category"]
            item["amount"] = str(new_details["amount"])
            item["description"] = new_details["description"]

            if save_expenses(expenses):
                print("Expense updated successfully!")
                return True

            return False

    print("Expense ID not found.")
    return False
