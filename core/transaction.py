from datetime import datetime

class Transaction:
    def __init__(self, account_number: str, type_: str, amount: float):
        self.account_number = account_number
        self.type = type_
        self.amount = amount
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"{self.timestamp} - {self.type}: {self.amount}"
