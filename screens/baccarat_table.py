# Description: This file contains the BaccaratTable class, which is a subclass of ttk.Frame.


import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from state.game_state import GameState  
from baccaratgame import BaccaratGame


class BaccaratTable(ttk.Frame):
    def __init__(self, master, game_state):
        super().__init__(master)
        self.master = master
        self.game_state = game_state
        self.pack()

        # Create canvas instead of main container
        self.canvas = ttk.Canvas(self, width=1600, height=1200)  # adjust size as needed
        self.canvas.pack(expand=True, fill="both")

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

        
        # Create the layout sections
        self.create_header()
        self.create_player_area()
        self.create_banker_area()
        self.create_result_area()
        self.create_controls()
        
        # Pack the main frame
        self.pack(expand=True, fill="both")

    def create_header(self):
        style = ttk.Style()
        style.configure('Header.TLabel',
            font=('Times New Roman', 36, 'bold'),
            padding=10,
            foreground='blue',
            background='white',
            relief='raised',
            borderwidth=3)
        
        self.header = ttk.Label(self,
            text="Baccarat", 
            style='Header.TLabel')  # Use the custom style
        self.header.place(x=512, y=50, anchor="center")

    def create_player_area(self):
        # Create LabelFrame with same styling
        self.player_box = ttk.LabelFrame(self, text="Player", padding="40 20", width=1000, height=200)
        self.player_box.pack_propagate(False)  # Prevent resizing
        
        # Add message label inside the box (still using pack here since it's inside the frame)
        self.player_message = ttk.Label(self.player_box, text="No cards yet", font=("Arial", 18))
        self.player_message.pack(expand=True)
        
        # Place the entire LabelFrame on canvas
        self.canvas.create_window(800, 400, window=self.player_box)

    def create_banker_area(self):
        self.banker_box = ttk.LabelFrame(self, text="Banker", padding="20 20", width=1000, height=200)
        self.banker_box.pack_propagate(False)
        
        self.banker_message = ttk.Label(self.banker_box, text="No cards yet", font=("Arial", 18))
        self.banker_message.pack(expand=True)

        self.canvas.create_window(800, 650, window=self.banker_box)

    def create_result_area(self):
        self.winner_box = ttk.LabelFrame(self, text="Winner", padding="20 20", width=1000, height=200)
        self.winner_box.pack_propagate(False)
        
        self.winner_message = ttk.Label(self.winner_box, text="Game not started", font=("Arial", 18))
        self.winner_message.pack(expand=True)

        self.canvas.create_window(800, 900, window=self.winner_box)

    def create_controls(self):
        self.button_frame = ttk.Frame(self)
        
        # Using ttkbootstrap's built-in styles
        self.continue_button = ttk.Button(
            self.button_frame, 
            text="Continue",
            style='success.TButton',
            command=self.on_continue  # You'll need to create this method
        )
        self.continue_button.pack(side="left", padx=10)

        self.exit_button = ttk.Button(
            self.button_frame, 
            text="Exit",
            style='danger.TButton',
            command=self.return_to_lobby
        )
        self.exit_button.pack(side="left", padx=10)

        # Adjust the position - try different coordinates
        self.canvas.create_window(800, 1050, window=self.button_frame)

        self.setup_exit_handling()

    def setup_exit_handling(self):
        self.master.bind('<Escape>', self.return_to_lobby)
        self.exit_button.config(command=self.return_to_lobby)

    def return_to_lobby(self):
        self.game_state['current_screen'] = 'casino_lobby'
        from screens.casino_lobby import CasinoLobby
        CasinoLobby(self.master, self.game_state)
        self.destroy()

    def on_continue(self):
        self.game_state['current_screen'] = 'baccarat_table'
        # Create an instance of BaccaratGame
        self.app_state = GameState()
        self.game = BaccaratGame()

        # call start_game method from BaccaratGame
        self.start_game(self.game_state)
        
        

    def update_display(self):
        # Update player cards display
        if self.app_state.player_cards:
            player_cards_text = ", ".join(str(card) for card in self.app_state.player_cards)
            self.player_message.config(text=f"Cards: {player_cards_text}")

        # Update banker cards display
        if self.app_state.banker_cards:
            banker_cards_text = ", ".join(str(card) for card in self.app_state.banker_cards)
            self.banker_message.config(text=f"Cards: {banker_cards_text}")

        # Update winner display
        if self.app_state.winner:
            self.winner_message.config(text=f"Winner: {self.app_state.winner}")