
def show_total(expenses):
    total = sum(float(item["amount"]) for item in expenses)

    print("\n----- TOTAL SPENDING -----")
    print(f"Total expenses: Rs. {total:.2f}")


def show_category_summary(expenses):
    print("\n----- CATEGORY SUMMARY -----")

    if not expenses:
        print("No expenses to summarize.")
        return

    summary = {}

    for item in expenses:
        category = item["category"]
        amount = float(item["amount"])

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")

