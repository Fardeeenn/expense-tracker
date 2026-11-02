from dataclasses import dataclass

@dataclass
class Expense:
    item: str
    amount: float
    category: str