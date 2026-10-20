from expense_tracker.models import Expense


def add_expense(expenses, item, amount):
    e = Expense(item=item, amount=amount)
    expenses.append(e)


def total_expenses(expenses):
    amounts = []
    for e in expenses:
        amounts.append(e.amount)
    return sum(amounts)