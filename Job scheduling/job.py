class Job:
    def __init__(self, profit, deadline) -> None:
        self.profit = profit
        self.deadline = deadline


    def __repr__(self) -> str:
        return f'Profit: {self.profit}, Deadline: {self.deadline}'

    def __str__(self) -> str:
        return f'Profit: {self.profit}, Deadline: {self.deadline}'
