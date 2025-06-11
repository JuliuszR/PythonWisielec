from tkinter import Toplevel, ttk
import tkinter as tk
from auth import User


class StatsWindow(tk.Toplevel):
    """
    Okno ze statystykami
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Statystyki graczy")
        self.geometry("500x400")
        self.resizable(False, False)

        self.configure(bg="#1a1a1a")

        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2a2a2a",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#2a2a2a",
                        font=("Segoe UI", 12))
        style.configure("Treeview.Heading",
                        background="#444",
                        foreground="white",
                        font=("Segoe UI", 12, "bold"))
        style.map("Treeview",
                  background=[("selected", "#660000")])

        header = tk.Label(self, text="Statystyki graczy", font=("Segoe UI", 16, "bold"), fg="white", bg="#1a1a1a")
        header.pack(pady=(10, 0))

        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame, columns=("login", "wins"), show="headings", height=10)
        self.tree.heading("login", text="Login")
        self.tree.heading("wins", text="Wygrane")
        self.tree.column("login", anchor="center", width=250)
        self.tree.column("wins", anchor="center", width=100)

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        close_btn = ttk.Button(self, text="Zamknij", command=self.destroy)
        close_btn.pack(pady=10)

        self.populate_stats()

    def populate_stats(self):
        """
        Wprowadzenie statystyk z bazy danych
        :return:
        """
        self.tree.delete(*self.tree.get_children())
        for user in User.select().order_by(User.wins.desc(), User.login.asc()):
            self.tree.insert("", "end", values=(user.login, user.wins))
