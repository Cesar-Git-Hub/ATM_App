import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from utils.validators import validate_amount
from utils.logger import log_action
from core.transaction import Transaction

class Dashboard:
    def __init__(self, account, main_root):
        self.account = account
        self.main_root = main_root
        self.transactions = []  # historial en memoria

        # Usamos Toplevel en lugar de Window
        self.root = tb.Toplevel()
        self.root.title("ATM Dashboard")
        self.root.geometry("700x500")

        # Bienvenida con nombre del cliente
        tb.Label(self.root, text=f"Bienvenido, {self.account.name}", 
                 font=("Segoe UI", 16, "bold"), bootstyle=PRIMARY).pack(pady=10)

        # Balance
        self.balance_label = tb.Label(self.root, 
                                      text=f"Balance: {self.account.get_balance():.2f}", 
                                      bootstyle=INFO)
        self.balance_label.pack(pady=5)

        # Botones compactos
        frame_buttons = tb.Frame(self.root)
        frame_buttons.pack(pady=10)

        tb.Button(frame_buttons, text="💰 Depositar", bootstyle=SUCCESS, width=12,
                  command=self.open_deposit_window).grid(row=0, column=0, padx=5)
        tb.Button(frame_buttons, text="💸 Retirar", bootstyle=DANGER, width=12,
                  command=self.open_withdraw_window).grid(row=0, column=1, padx=5)
        tb.Button(frame_buttons, text="📊 Balance", bootstyle=INFO, width=12,
                  command=self.show_balance).grid(row=0, column=2, padx=5)
        tb.Button(frame_buttons, text="❌ Salir", bootstyle=SECONDARY, width=12,
                  command=self.exit_app).grid(row=0, column=3, padx=5)

        # Treeview de movimientos
        columns = ("tipo", "monto", "fecha")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=8)
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("monto", text="Monto")
        self.tree.heading("fecha", text="Fecha")
        self.tree.pack(pady=10, fill=X)

    # ---------------------------
    # Ventanas secundarias
    # ---------------------------
    def open_deposit_window(self):
        win = tb.Toplevel(self.root)
        win.title("Depositar")
        win.geometry("300x150")

        tb.Label(win, text="Monto a depositar:").pack(pady=5)
        amount_entry = tb.Entry(win)
        amount_entry.pack(pady=5)

        tb.Button(win, text="Confirmar", bootstyle=SUCCESS,
                  command=lambda: self.deposit(amount_entry.get(), win)).pack(pady=10)

    def open_withdraw_window(self):
        win = tb.Toplevel(self.root)
        win.title("Retirar")
        win.geometry("300x150")

        tb.Label(win, text="Monto a retirar:").pack(pady=5)
        amount_entry = tb.Entry(win)
        amount_entry.pack(pady=5)

        tb.Button(win, text="Confirmar", bootstyle=DANGER,
                  command=lambda: self.withdraw(amount_entry.get(), win)).pack(pady=10)

    # ---------------------------
    # Lógica de operaciones
    # ---------------------------
    def deposit(self, amount_str, window):
        amount = validate_amount(amount_str)
        if amount and self.account.deposit(amount):
            log_action(f"Deposit {amount} to {self.account.name}")
            self.add_transaction("Depósito", amount)
            window.destroy()
        self.update_balance()

    def withdraw(self, amount_str, window):
        amount = validate_amount(amount_str)
        if amount and self.account.withdraw(amount):
            log_action(f"Withdraw {amount} from {self.account.name}")
            self.add_transaction("Retiro", amount)
            window.destroy()
        self.update_balance()

    def show_balance(self):
        self.add_transaction("Consulta Balance", self.account.get_balance())

    def update_balance(self):
        self.balance_label.config(text=f"Balance: {self.account.get_balance():.2f}")

    # ---------------------------
    # Historial de movimientos
    # ---------------------------
    def add_transaction(self, tipo, monto):
        tx = Transaction(self.account.name, tipo, monto)
        self.transactions.append(tx)
        self.tree.insert("", "end", values=(tx.type, f"{tx.amount:.2f}", tx.timestamp.strftime("%Y-%m-%d %H:%M:%S")))

    # ---------------------------
    # Confirmación de salida
    # ---------------------------
    def exit_app(self):
        confirm = messagebox.askyesno("Confirmar salida", "¿Seguro que deseas salir del ATM?")
        if confirm:
            self.root.destroy()
            self.main_root.destroy()  # 🔑 cerrar también el root principal
