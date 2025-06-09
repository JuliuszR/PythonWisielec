import tkinter as tk
import random
from ormpw import Haslo

class HangmanWindow:
    def __init__(self, haslo=None):
        self.window = tk.Toplevel()
        self.window.title("Wisielec")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        self.haslo = haslo.upper() if haslo else self.losuj_haslo().upper()
        self.odkryte = ['_' if c != ' ' else ' ' for c in self.haslo]
        self.ilosc_prob = 10
        self.uzyte_litery = set()

        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="#1a1a1a")
        self.canvas.pack(fill="both", expand=True)

        self.word_label = tk.Label(self.window, text=" ".join(self.odkryte), font=("Consolas", 24), fg="white", bg="#1a1a1a")
        self.canvas.create_window(400, 100, window=self.word_label)

        self.guess_entry = tk.Entry(self.window, font=("Arial", 18))
        self.canvas.create_window(400, 180, window=self.guess_entry)

        self.guess_btn = tk.Button(self.window, text="Zgadnij", command=self.zgadnij)
        self.canvas.create_window(400, 220, window=self.guess_btn)

        self.status_var = tk.StringVar()
        self.status_var.set(f"Pozostałe próby: {self.ilosc_prob}")
        self.status_label = tk.Label(self.window, textvariable=self.status_var, fg="white", bg="#1a1a1a", font=("Arial", 14))
        self.canvas.create_window(400, 260, window=self.status_label)

        self.used_var = tk.StringVar()
        self.used_var.set("Użyte litery: ")
        self.used_label = tk.Label(self.window, textvariable=self.used_var, fg="white", bg="#1a1a1a", font=("Arial", 12))
        self.canvas.create_window(400, 300, window=self.used_label)

    def losuj_haslo(self):
        wszystkie = list(Haslo.select())
        if not wszystkie:
            return "BRAK HASLA"
        return random.choice(wszystkie).tekst

    def zgadnij(self):
        litera = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if not litera or len(litera) != 1 or not litera.isalpha():
            return

        if litera in self.uzyte_litery:
            return

        self.uzyte_litery.add(litera)

        if litera in self.haslo:
            for i, c in enumerate(self.haslo):
                if c == litera:
                    self.odkryte[i] = litera
        else:
            self.ilosc_prob -= 1

        self.word_label.config(text=" ".join(self.odkryte))
        self.status_var.set(f"Pozostałe próby: {self.ilosc_prob}")
        self.used_var.set("Użyte litery: " + ", ".join(sorted(self.uzyte_litery)))

        if "_" not in self.odkryte:
            self.status_var.set("Gratulacje! Wygrałeś.")
            self.guess_btn.config(state="disabled")
        elif self.ilosc_prob == 0:
            self.status_var.set(f"Przegrałeś! Hasło to: {self.haslo}")
            self.guess_btn.config(state="disabled")
