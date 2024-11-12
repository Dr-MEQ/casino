import tkinter as tk
from PIL import Image, ImageTk  # For handling graphics
from tkinter import font  # For custom fonts if needed
from screens.casino_lobby import CasinoLobby  # For the transition to lobby

class CasinoEntrance(tk.Frame):
    def __init__(self, master, app_state):
        super().__init__(master)
        self.master = master
        self.app_state = app_state

        self.master.geometry("1024x768")
        self.master.configure(bg='black')
        self.master.title("Casino Entrance")

        self.load_graphics()  # Load background first
        self.setup_ui()      # Then add UI elements on top
        self.pack(fill="both", expand=True)

    def load_graphics(self):
        try:
            #print("Attempting to load image...")
            self.bg_image = Image.open("assets/images/casino_opening_screen.png")
            #print("Image loaded successfully")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.background_label = tk.Label(self, image=self.bg_photo, bg='red')
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            #print("Background placed")
        except FileNotFoundError:
            print("Image file not found")

                                        
    def setup_ui(self):
        # Welcome message centered at top third
        self.welcome_label = tk.Label(self, 
            text="Welcome to the Casino",
            font=("Arial", 32, "bold"),
            bg='black',  # We can adjust these colors
            fg='gold')
        self.welcome_label.place(relx=0.5, rely=0.1, anchor='center')

         
        # Buttons centered in bottom third
        button_style = {
            'font': ('Arial', 14),
            'width': 15,
            'height': 2,
            'bg': 'gold',
            'fg': 'black'
        }

        self.enter_button = tk.Button(self, 
            text="Enter Casino",
            command=self.enter_casino,
            **button_style)

        self.exit_button = tk.Button(self, 
            text="Exit",
            command=self.exit_casino,
            **button_style)

        self.enter_button.place(relx=0.5, rely=0.7, anchor='center')
        self.exit_button.place(relx=0.5, rely=0.8, anchor='center')
          
      
    def enter_casino(self):
        self.destroy()  # Clear entrance screen
        CasinoLobby(self.master, self.app_state)  # Transition to lobby
    
    def exit_casino(self):
        self.master.destroy()