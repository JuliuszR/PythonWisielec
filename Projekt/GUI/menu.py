import tkinter as tk
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

        self.start_button = tk.Button(self.master, text="Nowa Gra", font=("Helvetica", 14, "bold"))
        self.start_button_window = self.canvas.create_window(400, 300, anchor="center", window=self.start_button)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuWindow(root)
    root.mainloop()
