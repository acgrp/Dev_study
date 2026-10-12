from expense import Expense
from repository import JsonExpenseRepository

repository = JsonExpenseRepository("data/expenses.json")
expenses = [Expense(1, "2026-10-12", "food", 12000)]

repository.save_all(expenses)
print(repository.find_all())