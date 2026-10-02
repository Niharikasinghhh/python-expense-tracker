
from expense import get_expense_details
from storage import (
    initialize_file,
    load_expenses,
    add_expense,
    delete_expense,
    update_expense
)
from reports import show_total, show_category_summary


def view_expenses():
    expenses = load_expenses()

    print("\n----- ALL EXPENSES -----")

    if not expenses:
        print("No expenses found.")
        return

    for item in expenses:
        print(
            f"ID: {item['id']} | "
            f"Date: {item['date']} | "
            f"Category: {item['category']} | "
            f"Amount: Rs. {item['amount']} | "
            f"Description: {item['description']}"
        )


def search_category():
    category = input("Enter category to search: ").strip().lower()
    expenses = load_expenses()

    found = False

    for item in expenses:
        if item["category"].lower() == category:
            print(item)
            found = True

    if not found:
        print("No expenses found in this category.")


def add_new_expense():
    try:
        details = get_expense_details()
        add_expense(details)

    except ValueError as error:
        print("Invalid input:", error)


def edit_expense():
    expense_id = input("Enter expense ID to edit: ").strip()

    try:
        print("Enter the new details:")
        details = get_expense_details()
        update_expense(expense_id, details)

    except ValueError as error:
        print("Invalid input:", error)


def main():
    initialize_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Total Spending")
        print("7. Category Summary")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_new_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            edit_expense()

        elif choice == "5":
            expense_id = input(
                "Enter expense ID to delete: "
            ).strip()
            delete_expense(expense_id)

        elif choice == "6":
            show_total(load_expenses())

        elif choice == "7":
            show_category_summary(load_expenses())

        elif choice == "8":
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
