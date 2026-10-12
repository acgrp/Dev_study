from expense import Expense

expense = Expense(1, "2026-10-12", "food", 12000, "lunch")
print(expense.id)
print(expense.date)
print(expense.category)
print(expense.amount)
print(expense.memo)