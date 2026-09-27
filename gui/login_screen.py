import ttkbootstrap as tb
from ttkbootstrap.constants import *
from core.database import Database
from gui.dashboard import Dashboard

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Login")
        self.root.geometry("350x250")

        self.db = Database()

        tb.Label(self.root, text="Bienvenido al ATM", 
                 font=("Segoe UI", 16, "bold"), bootstyle=PRIMARY).pack(pady=10)

        tb.Label(self.root, text="Nombre de cliente:", bootstyle=INFO).pack(pady=5)
        self.name_entry = tb.Entry(self.root, width=25)
        self.name_entry.pack(pady=5)

        tb.Label(self.root, text="PIN:", bootstyle=INFO).pack(pady=5)
        self.pin_entry = tb.Entry(self.root, show="*", width=25)
        self.pin_entry.pack(pady=5)

        tb.Button(self.root, text="Iniciar Sesión", bootstyle=SUCCESS, 
                  command=self.login).pack(pady=15)

        self.message_label = tb.Label(self.root, text="", bootstyle=WARNING)
        self.message_label.pack(pady=5)

    def login(self):
        name = self.name_entry.get().strip()
        pin = self.pin_entry.get().strip()
        account = self.db.get_account(name)

        if account and account.validate_pin(pin):
            self.message_label.config(text="✅ Login correcto", bootstyle=SUCCESS)
            self.root.withdraw()  # ocultar login
            Dashboard(account, self.root)  # pasar root al Dashboard
        else:
            self.message_label.config(text="❌ Credenciales inválidas", bootstyle=DANGER)
