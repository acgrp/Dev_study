from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Expense:
    id: int
    date: str
    category: str
    amount: int
    memo: str = ""

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Expense":
        return cls(
            id=int(data["id"]),
            date=str(data["date"]),
            category=str(data["category"]),
            amount=int(data["amount"]),
            memo=str(data.get("memo", ""))
        )