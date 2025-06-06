import tkinter as tk
from tkinter import ttk, PhotoImage
import os
from PIL import Image, ImageTk

class MainMenuWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("WISIELEC")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        image_path = os.path.join(parent_dir, "Assets", "wisielec.png")

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")


        image_path = os.path.join(parent_dir, "Assets", "nowaGra.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.new_game_image = ImageTk.PhotoImage(button_img)

        image_path = os.path.join(parent_dir, "Assets", "logowanie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.logowanie_image = ImageTk.PhotoImage(button_img)

        image_path = os.path.join(parent_dir, "Assets", "wyjscie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.wyjscie_image = ImageTk.PhotoImage(button_img)

        self.button_id = self.canvas.create_image(400, 260, image=self.new_game_image)
        self.button_logowanie = self.canvas.create_image(400, 320, image=self.logowanie_image)
        self.button_wyjscie = self.canvas.create_image(400, 380, image=self.wyjscie_image)

        self.canvas.tag_bind(self.button_id, "<Button-1>", self.start_new_game)
        self.canvas.tag_bind(self.button_logowanie, "<Button-1>", self.logowanie)
        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.wyjscie)

    def start_new_game(self, event):
        print("Nowa gra kliknięta!")

    def wyjscie(self, event):
        print("Wyjscie")

    def logowanie(self, event):
        print("Logowanie")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuWindow(root)
    root.mainloop()
