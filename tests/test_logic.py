from expense_tracker.models import Expense
from expense_tracker.logic import add_expense, total_expenses

def test_add_expense():
    expenses = []
    add_expense(expenses, "chai", 20)
    assert len(expenses) == 1
    assert expenses[0].item == "chai"
    assert expenses[0].amount == 20

def test_total_expenses():
    expenses = []
    add_expense(expenses, "chai", 20)
    add_expense(expenses, "samosa", 15)
    total = total_expenses(expenses)
    assert total == 35





