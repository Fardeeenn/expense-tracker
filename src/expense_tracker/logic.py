from expense_tracker.models import Expense


def add_expense(expenses: list[Expense], item: str, amount: float, category: str) -> None:
    e = Expense(item=item, amount=amount, category=category)
    expenses.append(e)


def total_expenses(expenses: list[Expense]) -> float:
    amounts = []
    for e in expenses:
        amounts.append(e.amount)
    return sum(amounts)