from datetime import date

from errors import ExpenseValidationError
from expense import Expense
from repository import JsonExpenseRepository


class ExpenseService:
    def __init__(self, repository: JsonExpenseRepository):
        self.repository = repository

    def add_expense(
            self,
            date_text: str,
            category: str,
            amount_text: str,
            memo: str = "",
    ) -> Expense:
        date_text = date_text.strip()
        category = category.strip().lower()
        memo = memo.strip()

        try:
            date.fromisoformat(date_text)
        except ValueError as error:
            raise ExpenseValidationError(
                "Use YYYY-MM-DD for the date."
            ) from error

        if not category:
            raise ExpenseValidationError(
                "Category is required."
            )

        try:
            amount = int(amount_text)
        except (TypeError, ValueError) as error:
            raise ExpenseValidationError(
                "Amount must be a number."
            ) from error

        if amount <= 0:
            raise ExpenseValidationError(
                "Amount must be greater than zero."
            )

        expenses = self.repository.find_all()
        next_id = max(
            (expense.id for expense in expenses),
            default=0,
        ) + 1
        expense = Expense(
            next_id,
            date_text,
            category,
            amount,
            memo,
        )
        expenses.append(expense)
        self.repository.save_all(expenses)
        return expense


    def list_expenses(
            self,
            category: str | None = None,
    ) -> list[Expense]:
        expenses = self.repository.find_all()

        if category:
            key = category.strip().lower()
            expenses = [
                item
                for item in expenses
                if item.category == key
            ]

        return sorted(
            expenses,
            key=lambda item: (item.date, item.id),
        )


    def totals_by_category(self) -> dict[str, int]:
        totals: dict[str, int] = {}

        for expense in self.repository.find_all():
            totals[expense.category] = (
                totals.get(expense.category, 0)
                + expense.amount
            )

        return totals
