import tkinter as tk
import os
from PIL import Image, ImageTk

class HangmanWindow:
    def __init__(self, master = None):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Hangman Window")
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

    def on_close(self):
        self.master.deiconify()
        self.window.destroy()
