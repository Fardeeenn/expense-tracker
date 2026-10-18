import json


def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as f:
        json.dump(expenses, f ,indent=2)


def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as f:
          return json.load(f)
    except FileNotFoundError:
        return []


