class Item:
    def __init__(self, profit, weight) -> None:
        self.profit = profit
        self.weight = weight

    def __str__(self) -> str:
        return f"Profit: {self.profit}, Weight: {self.weight}"

    def __repr__(self) -> str:
        return f"Profit: {self.profit}, Weight: {self.weight}"