from expense_tracker.models import Expense
from expense_tracker.storage import load_expenses,save_expenses
from expense_tracker.logic import add_expense,total_expenses


def main():
    print("Welcome to Expense Tracker !")
    expenses =load_expenses()
    while True:
        choice = input("Choose an option : add/list/total/quit")
        if choice == "add":
            item = input("Enter name of item")
            try:
                amount = float(input("Enter amount of item"))
                add_expense(expenses, item, amount)
            except ValueError:
                print("Please enter a valid number for amount")

        elif choice == "list":
            print(expenses)

        elif choice == "total":
            print(total_expenses(expenses))

        elif choice == "quit":
            save_expenses(expenses)
            break

if __name__ == "__main__":
    main()