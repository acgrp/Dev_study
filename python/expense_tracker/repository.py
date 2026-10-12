import json
from pathlib import Path

from expense import Expense

class JsonExpenseRepository:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def find_all(self) -> list[Expense]:
        if not self.file_path.exists():
            return []

        try:
            text = self.file_path.read_text(encoding="utf-8")
            raw_items = json.loads(text)
            if not isinstance(raw_items, list):
                raise ValueError("JSON root must be a list.")
            return [
                Expense.from_dict(item)
                for item in raw_items]

        except (
                OSError,
                ValueError,
                TypeError,
                KeyError,
                AttributeError
        ) as error:
            raise RuntimeError("Could not read expense data.") from error

    def save_all(self, expenses: list[Expense]) -> None:
        payload = [expense.to_dict() for expense in expenses]

        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.file_path.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except OSError as error:
            raise RuntimeError("Could not save expense data.") from error