import tkinter as tk
import os

from Projekt.GUI.NewGameWindow import NewGameWindow
from StatsWindow import StatsWindow
from PIL import Image, ImageTk

class LoggedInWindow:
    def __init__(self, master = None, user=None):
        self.master = master
        self.user = user
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

        self.canvas.tag_bind(self.button_id, "<Button-1>", self.start_new_game)
        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.exit)
        self.canvas.tag_bind(self.button_statystki, "<Button-1>", self.open_stats)

    def open_stats(self, event=None):
        win = StatsWindow(self.master)
        win.grab_set()
        win.focus_force()

    def on_close(self):
        self.master.deiconify()
        self.window.destroy()

    def exit(self, event = None):
        if self.master is not None:
            self.master.deiconify()
        self.window.destroy()

    def start_new_game(self, event=None):
        win = NewGameWindow(self.master, user=self.user)
        win.window.grab_set()
        win.window.focus_force()
        self.window.destroy()