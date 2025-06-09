import tkinter as tk
import os
from HangmanWindow import HangmanWindow
from PIL import Image, ImageTk

class NewGameWindow:
    def __init__(self, master = None, user=None):
        self.master = master
        self.user = user
        self.window = tk.Toplevel(master)
        self.window.title("New Game Window")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        image_path = os.path.join(parent_dir, "Assets", "wisielec.png")

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        #przyciski do wyboru gry trybu
        #1 gra gdzie ktos wymysla haslo
        image_path = os.path.join(parent_dir, "Assets", "tryb1.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.tryb1_image = ImageTk.PhotoImage(button_img)

        self.tryb1 = self.canvas.create_image(280, 290, image=self.tryb1_image )
        self.canvas.tag_bind(self.tryb1, "<Button-1>", self.ModeFirst)

        #2 gra haslo z bazy
        image_path = os.path.join(parent_dir, "Assets", "tryb2.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.tryb2_image  = ImageTk.PhotoImage(button_img)

        self.tryb2 = self.canvas.create_image(540, 290, image=self.tryb2_image )
        self.canvas.tag_bind(self.tryb2, "<Button-1>", self.ModeSecond)


        #wyjscie
        image_path = os.path.join(parent_dir, "Assets", "wyjscie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.wyjscie_image = ImageTk.PhotoImage(button_img)

        self.button_wyjscie = self.canvas.create_image(640, 540, image=self.wyjscie_image)
        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.exit)

    def on_close(self):
        self.master.deiconify()
        self.window.destroy()

    def exit(self, event = None):
        if self.master is not None:
            self.master.deiconify()
        self.window.destroy()

    def ModeFirst(self, event=None):
        def get_custom_word():
            popup = tk.Toplevel(self.window)
            popup.title("Wprowadź hasło")
            popup.geometry("400x200")
            popup.resizable(False, False)

            tk.Label(popup, text="Podaj hasło do zgadywania:", font=("Arial", 14)).pack(pady=10)
            entry = tk.Entry(popup, font=("Arial", 14))
            entry.pack(pady=10)

            def submit():
                word = entry.get().strip()
                if word:
                    popup.destroy()
                    self.window.withdraw()
                    self.hangman_window = HangmanWindow(user=self.user, haslo=word)

            submit_btn = tk.Button(popup, text="Rozpocznij grę", command=submit)
            submit_btn.pack(pady=10)

        get_custom_word()

    def ModeSecond(self, event=None):
        self.window.withdraw()
        self.hangman_window = HangmanWindow(user=self.user)
