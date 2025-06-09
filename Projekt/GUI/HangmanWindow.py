import tkinter as tk
import random
from ormpw import Haslo
from PIL import Image, ImageTk
import os

class HangmanWindow:
    def __init__(self, haslo=None, user=None):
        self.user = user
        self.window = tk.Toplevel()
        self.window.title("Wisielec")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.exit_back)

        print("Zalogowany:", self.user)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        image_path = os.path.join(parent_dir, "Assets", "wisielec.png")

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.haslo = haslo.upper() if haslo else self.losuj_haslo().upper()
        self.odkryte = ['_' if c != ' ' else ' ' for c in self.haslo]
        self.ilosc_prob = 6
        self.uzyte_litery = set()

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")


        self.word_label = tk.Label(self.window, text=" ".join(self.odkryte), font=("Consolas", 24), fg="white", bg="#1a1a1a")
        self.canvas.create_window(400, 190, window=self.word_label)

        self.guess_entry = tk.Entry(self.window, font=("Arial", 18))
        self.canvas.create_window(400, 260, window=self.guess_entry)

        self.guess_btn = tk.Button(self.window, text="Zgadnij", command=self.zgadnij)
        self.canvas.create_window(400, 300, window=self.guess_btn)

        self.status_var = tk.StringVar()
        self.status_label = tk.Label(self.window, textvariable=self.status_var, fg="white", bg="#1a1a1a", font=("Arial", 14))
        self.canvas.create_window(400, 360, window=self.status_label)

        self.used_var = tk.StringVar()
        self.used_var.set("Użyte litery: ")
        self.used_label = tk.Label(self.window, textvariable=self.used_var, fg="white", bg="#1a1a1a", font=("Arial", 12))
        self.canvas.create_window(400, 420, window=self.used_label)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        heart_path = os.path.join(parent_dir, "Assets", "serce.png")

        heart_img = Image.open(heart_path)
        heart_img = heart_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.heart_photo = ImageTk.PhotoImage(heart_img)

        self.serca = []

        for i in range(self.ilosc_prob):
            x = 700 - i * 45
            y = 50
            heart_id = self.canvas.create_image(x, y, image=self.heart_photo)
            self.serca.append(heart_id)

        self.window.focus_force()
        self.window.grab_set()

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
            if self.serca:
                to_remove = self.serca.pop()
                self.canvas.delete(to_remove)

        self.word_label.config(text=" ".join(self.odkryte))
        self.used_var.set("Użyte litery: " + ", ".join(sorted(self.uzyte_litery)))


        if "_" not in self.odkryte:
            self.status_var.set("Gratulacje! Wygrałeś.")
            self.guess_btn.config(state="disabled")
            if self.user:
                self.user.wins += 1
                self.user.save()
                self.close_btn = tk.Button(self.window, text="Zamknij", command=self.exit_back)
                self.canvas.create_window(400, 500, window=self.close_btn)
        elif self.ilosc_prob == 0:
            self.status_var.set(f"Przegrałeś! Hasło to: {self.haslo}")
            self.guess_btn.config(state="disabled")
            self.close_btn = tk.Button(self.window, text="Zamknij", command=self.exit_back)
            self.canvas.create_window(400, 500, window=self.close_btn)



    def exit_back(self):
        if self.window.master:
            self.window.master.deiconify()
        self.window.destroy()