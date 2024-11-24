import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk  # For handling graphics
from tkinter import font  # For custom fonts if needed
import tkinter.font as tkFont  # For custom fonts if needed
from screens.casino_lobby import CasinoLobby  # For the transition to lobby

class CasinoEntrance(tk.Frame):  # Change back to tk.Frame
    
    def __init__(self, master, game_state):
        super().__init__(master)
        self.master = master
        self.game_state = game_state
        self.load_graphics()
        self.setup_ui()
        self.pack(fill='both', expand=True)  # Add this line

    from tkinter import font

    def load_custom_font(self):
        try:
            custom_font = font.Font(
                family="Casino Queen",  # Exact name as shown in the font list
                size=96,
                weight="normal"
            )
            return custom_font
        except Exception as e:
            print(f"Font loading error: {e}")
            return font.Font(family="Arial", size=48)
        
    def load_graphics(self):
        try:
            self.bg_image = Image.open("assets/images/playing_card_back.png")
            # Resize to fit our window while maintaining aspect ratio
            self.bg_image = self.bg_image.resize((1600, 1200), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.background_label = tk.Label(self, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Image file not found")  # Added the missing except block content

                                        
    def setup_ui(self):
        # Welcome message centered at top third
        # At the start of your setup_ui method or in __init__



        style = ttk.Style()
        style.configure('Large.TButton', font=('Arial', 20))  # Adjust font size as needed
        
        casino_font = self.load_custom_font()
        custom_font = casino_font.copy()

        self.welcome_label = ttk.Label(
            self, 
            text="  Welcome to the Casino  ",
            font=custom_font,
            bootstyle="danger-inverse"
        )
        self.welcome_label.lift()  # Bring to front
        self.welcome_label.place(relx=0.5, rely=0.1, anchor='center')

        # Create a frame for buttons to ensure they're above background
        button_frame = ttk.Frame(self)
        button_frame.place(relx=0.5, rely=0.85, anchor='center')


        # Create a custom font
        self.enter_button = ttk.Button(
            button_frame,
            text="Enter Casino",
            command=self.enter_casino,
            bootstyle="primary",
            style='Large.TButton',
            width=30,
            padding=(40, 20)
        )
        self.enter_button.pack(pady=20)  # Add some vertical spacing

        self.exit_button = ttk.Button(
            button_frame,  # Parent is now button_frame
            text="Exit",
            command=self.exit_casino,
            bootstyle="danger",
            style='Large.TButton',
            width=30,
            padding=(40, 20)
        )

        self.exit_button.pack(pady=20)  # Add some vertical spacing
          
      
    def enter_casino(self):
        self.pack_forget()  # Remove from view first
        self.destroy()      # Then destroy
        self.game_state['current_screen'] = 'casino_lobby'
        lobby = CasinoLobby(self.master, self.game_state)  
        lobby.pack(fill="both", expand=True)
    
    def exit_casino(self):
        self.game_state['current_screen'] = 'exit'
        self.master.destroy()