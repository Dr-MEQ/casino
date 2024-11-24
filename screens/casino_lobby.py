import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from state.game_state import GameState


class CasinoLobby(ttk.Frame):
    def __init__(self, master, game_state):
        super().__init__(master)
        self.master = master
        self.game_state = game_state
        
        self.master.title("Casino Lobby")
        self.load_graphics()
        self.setup_ui()
        self.pack(fill="both", expand=True)

        style = ttk.Style()

    def load_graphics(self):
        try:
            self.bg_image = Image.open("assets/images/casino_opening_screen.png")
            # Resize the image while maintaining aspect ratio
            self.bg_image = self.bg_image.resize((1600, 1200), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
            # Use ttk.Label instead of tk.Label
            self.background_label = ttk.Label(self, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        except FileNotFoundError:
            print("Image file not found")

    def setup_ui(self):
        
        # Configure the style for large buttons
        style = ttk.Style()
        style.configure('Large.TButton', 
            font=('Arial', 30, 'bold'),
            padding=10,
            foreground='white',
            background='blue',
            relief='raised',
            borderwidth=3)

        # Configure the style for balance display
        style = ttk.Style()
        style.configure('Balance.TLabel', 
            font=('Arial', 30, 'bold'),
            padding=10,
            foreground='green',
            relief='raised',
            borderwidth=3)
        
        # Configure the style for welcome message
        style = ttk.Style()
        style.configure('Welcome.TLabel', 
            font=('Arial', 40, 'italic'),
            padding=10,
            foreground='blue',
            background='white',
            relief='raised',
            borderwidth=3)

        # Balance display
        self.balance_label = ttk.Label(self,
            text=f"Balance: ${self.game_state['player_funds']}",
            style='Balance.TLabel')
        self.balance_label.place(relx=0.5, rely=0.05, anchor='center')

        # Welcome message
        self.welcome_label = ttk.Label(self, 
            text="Select a game to play",
            style='Welcome.TLabel')
        self.welcome_label.place(relx=0.25, rely=0.2, anchor='center')

        # Game buttons
        # For active games
        self.baccarat_btn = ttk.Button(self, 
            text="Baccarat", 
            command=self.play_baccarat,
            style='Large.TButton',
            width=20)
        self.baccarat_btn.place(relx=0.35, rely=0.4, anchor='center')

        # For inactive/coming soon games
        self.blackjack_btn = ttk.Button(self, 
            text="Blackjack (Coming Soon)", 
            style='Large.TButton',
            width=20,
            state='disabled')
        self.blackjack_btn.place(relx=0.45, rely=0.5, anchor='center')

        self.poker_btn = ttk.Button(self, 
            text="Poker (Coming Soon)", 
            style='Large.TButton',
            width=20,
            state='disabled')
        self.poker_btn.place(relx=0.55, rely=0.6, anchor='center')

        self.roulette_btn = ttk.Button(self, 
            text="Roulette (Coming Soon)", 
            style='Large.TButton',
            width=20,
            state='disabled')
        self.roulette_btn.place(relx=0.65, rely=0.7, anchor='center')

        # Configure the style for exit button
        style = ttk.Style()
        style.configure('Exit.TButton', 
            font=('Arial', 20, 'bold'),
            padding=10,
            foreground='red',
            background='black',
            relief='raised',
            borderwidth=3)

        # Exit button
        self.exit_btn = ttk.Button(self, 
            text="Leave the Baccarat Table",
            command=self.exit_casino,
            style='Exit.TButton',
            width=30)
        self.exit_btn.place(relx=0.5, rely=0.9, anchor='center')

    def play_baccarat(self):
        self.game_state['current_screen'] = 'baccarat_table'
        from screens.baccarat_table import BaccaratTable
        self.destroy()
        BaccaratTable(self.master, self.game_state)

    # In lobby.py
    def exit_casino(self):
        from screens.casino_entrance import CasinoEntrance  # Import only happens when method is called
        self.game_state['current_screen'] = 'casino_entrance'
        CasinoEntrance(self.master, self.game_state)
        self.destroy()