import json
from dataclasses import asdict
from expense_tracker.models import Expense

def save_expenses(expenses: list[Expense]) -> None:
    data = [asdict(e) for e in expenses]
    with open("expenses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_expenses() -> list[Expense]:
    try:
        with open("expenses.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    return [Expense(**d) for d in data]