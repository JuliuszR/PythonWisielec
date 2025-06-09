import tkinter as tk
import os
from auth import *
from PIL import Image, ImageTk
from LoggedInWindow import LoggedInWindow
from NewGameWindow import NewGameWindow

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




        image_path = os.path.join(parent_dir, "Assets", "logowanie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.logowanie_image = ImageTk.PhotoImage(button_img)

        image_path = os.path.join(parent_dir, "Assets", "wyjscie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.wyjscie_image = ImageTk.PhotoImage(button_img)

        self.button_logowanie = self.canvas.create_image(400, 280, image=self.logowanie_image)
        self.button_wyjscie = self.canvas.create_image(400, 370, image=self.wyjscie_image)

        self.canvas.tag_bind(self.button_logowanie, "<Button-1>", lambda e : self.show_login_screen())
        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.wyjscie)



    def show_login_screen(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.login_entry = tk.Entry(self.master, font=("Arial", 14))
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 14))

        self.canvas.create_text(400, 180, text="Login", fill="white", font=("Arial", 18, "bold"))
        self.canvas.create_window(400, 210, window=self.login_entry)

        self.canvas.create_text(400, 260, text="Hasło", fill="white", font=("Arial", 18, "bold"))
        self.canvas.create_window(400, 290, window=self.password_entry)

        self.login_btn = tk.Button(self.master, text="Zaloguj", command=self.try_login)
        self.canvas.create_window(350, 350, window=self.login_btn)

        self.register_btn = tk.Button(self.master, text="Zarejestruj", command=self.try_register)
        self.canvas.create_window(450, 350, window=self.register_btn)

        self.message_var = tk.StringVar()
        self.message_label = tk.Label(self.master, textvariable=self.message_var, fg="red", bg="black")
        self.canvas.create_window(400, 400, window=self.message_label)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)

        image_path = os.path.join(parent_dir, "Assets", "wyjscie.png")
        button_img = Image.open(image_path)
        button_img = button_img.resize((210, 100), Image.Resampling.LANCZOS)
        self.wyjscie_image = ImageTk.PhotoImage(button_img)

        self.button_powrot = self.canvas.create_image(640, 540, image=self.wyjscie_image)
        self.canvas.tag_bind(self.button_powrot, "<Button-1>", self.back_to_main_menu)


    def try_login(self):
        login_input = self.login_entry.get()
        password = self.password_entry.get()

        success, result = login(login_input, password)
        if success:
            self.message_var.set("Zalogowano jako " + result.login)

            self.master.withdraw()
            self.loggedInWindow = LoggedInWindow(self.master, user=result)
        else:
            self.message_var.set(result)

    def try_register(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        success, msg = register(login, password)
        self.message_var.set(msg)

    def back_to_main_menu(self, event=None):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.button_logowanie = self.canvas.create_image(400, 320, image=self.logowanie_image)
        self.button_wyjscie = self.canvas.create_image(400, 380, image=self.wyjscie_image)

        self.canvas.tag_bind(self.button_logowanie, "<Button-1>", lambda e: self.show_login_screen())
        self.canvas.tag_bind(self.button_wyjscie, "<Button-1>", self.wyjscie)

    def start_new_game(self, event):
        self.master.withdraw()

        win = NewGameWindow(self.master, user=self.user)

    def wyjscie(self, event):
        self.master.destroy()

    def logowanie(self, event):
        print("Logowanie")

    #def exit(self, event = None):
     #   self.master.deiconify()
      #  self.master.destroy()


