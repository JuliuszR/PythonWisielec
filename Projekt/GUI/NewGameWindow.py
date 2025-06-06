import tkinter as tk
import os
from PIL import Image, ImageTk

class NewGameWindow:
    def __init__(self, master = None):
        self.window = tk.Toplevel(master)
        self.window.title("New Game Window")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        image_path = os.path.join(parent_dir, "Assets", "wisielec.png")

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        image_path = os.path.join(parent_dir, "Assets", "rejestracja.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.rejestracja = ImageTk.PhotoImage(button_img)

        self.button_id = self.canvas.create_image(400, 260, image=self.rejestracja)

        self.window.mainloop()