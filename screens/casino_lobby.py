import tkinter as tk
from PIL import Image, ImageTk
from state.game_state import GameState  # Add this import

class CasinoLobby(tk.Frame):
    def __init__(self, master, app_state):
        super().__init__(master)
        self.master = master
        self.app_state = app_state
        
        self.master.title("Casino Lobby")
        self.load_graphics()
        self.setup_ui()
        self.pack(fill="both", expand=True)

    def load_graphics(self):
        try:
            # For now, using same background
            self.bg_image = Image.open("assets/images/casino_opening_screen.png")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.background_label = tk.Label(self, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Image file not found")

    def setup_ui(self):
        # Balance display at top
        self.balance_label = tk.Label(self,
            text=f"Balance: ${self.app_state.state['player_funds']}",
            font=("Arial", 24, "bold"),
            fg='gold',
            bg='black')
        self.balance_label.place(relx=0.5, rely=0.05, anchor='center')

        # Game option styles
        active_style = {
            'font': ('Arial', 16),
            'width': 20,
            'height': 3,
            'bg': 'gold',
            'fg': 'black'
        }
        
        inactive_style = {
            'font': ('Arial', 16, 'italic'),
            'width': 20,
            'height': 3,
            'bg': 'gray50',
            'fg': 'black',
            'state': 'disabled'
        }

        # Game buttons
        self.baccarat_btn = tk.Button(self, text="Baccarat", command=self.play_baccarat, **active_style)
        self.baccarat_btn.place(relx=0.35, rely=0.4, anchor='center')

        self.blackjack_btn = tk.Button(self, text="Blackjack", **inactive_style)
        self.blackjack_btn.place(relx=0.65, rely=0.4, anchor='center')

        self.poker_btn = tk.Button(self, text="Poker", **inactive_style)
        self.poker_btn.place(relx=0.35, rely=0.6, anchor='center')

        self.roulette_btn = tk.Button(self, text="Roulette", **inactive_style)
        self.roulette_btn.place(relx=0.65, rely=0.6, anchor='center')

        # Exit button at bottom
        self.exit_btn = tk.Button(self, 
            text="Exit Casino",
            command=self.exit_casino,
            font=('Arial', 14),
            bg='darkred',
            fg='white')
        self.exit_btn.place(relx=0.5, rely=0.9, anchor='center')

        # Optional: Welcome message
        self.welcome_label = tk.Label(self,
            text="Select a Game to Play",
            font=("Arial", 20, "bold"),
            fg='white',
            bg='black')
        self.welcome_label.place(relx=0.5, rely=0.15, anchor='center')

    def play_baccarat(self):
        from screens.baccarat_table import BaccaratTable
        self.destroy()
        BaccaratTable(self.master, self.app_state)

    # In lobby.py
    def exit_casino(self):
        from screens.casino_entrance import CasinoEntrance  # Import only happens when method is called
        self.app_state.reset_game_state()
        CasinoEntrance(self.master, self.app_state)
        self.destroy()