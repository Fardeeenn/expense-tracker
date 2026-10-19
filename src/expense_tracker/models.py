from dataclasses import dataclass

@dataclass
class Expense:
    item: str
    amount: float


e = Expense(item="chai", amount=20)

