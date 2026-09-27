import tkinter as tk
from gui.login_screen import LoginScreen

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Aplicación cerrada manualmente.")
