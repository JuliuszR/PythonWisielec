import tkinter as tk
import os
from PIL import Image, ImageTk

class LoggedInWindow:
    def __init__(self, master = None):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Logged in Window")
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

        image_path = os.path.join(parent_dir, "Assets", "nowaGra.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.new_game_image = ImageTk.PhotoImage(button_img)

        image_path = os.path.join(parent_dir, "Assets", "statystyki.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.statystki_image = ImageTk.PhotoImage(button_img)

        image_path = os.path.join(parent_dir, "Assets", "wyjscie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.wyjscie_image = ImageTk.PhotoImage(button_img)

        self.button_id = self.canvas.create_image(400, 260, image=self.new_game_image)
        self.button_statystki = self.canvas.create_image(400, 320, image=self.statystki_image)
        self.button_wyjscie = self.canvas.create_image(400, 380, image=self.wyjscie_image)

        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.exit)

    def on_close(self):
        self.master.deiconify()
        self.window.destroy()

    def exit(self, event = None):
        if self.master is not None:
            self.master.deiconify()
        self.window.destroy()