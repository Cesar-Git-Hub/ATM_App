class Account:
    def __init__(self, name: str, pin: str, balance: float = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def validate_pin(self, entered_pin: str) -> bool:
        return self.pin == entered_pin

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance
