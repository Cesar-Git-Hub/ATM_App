import json
from core.account import Account

class Database:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return {acc["name"]: Account(**acc) for acc in data}
        except FileNotFoundError:
            return {}

    def save_accounts(self):
        data = [
            {"name": acc.name, "pin": acc.pin, "balance": acc.balance}
            for acc in self.accounts.values()
        ]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add_account(self, account: Account):
        self.accounts[account.name] = account
        self.save_accounts()

    def get_account(self, name: str) -> Account:
        return self.accounts.get(name)
