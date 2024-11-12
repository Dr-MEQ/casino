#import tkinter as tk
#from tkinter import Frame, BOTH
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from state.game_state import GameState  # Add this import


class BaccaratTable(tk.Frame):
    def __init__(self, master, app_state):
        super().__init__(master)
        self.master = master
        self.app_state = app_state
        self.pack()

        # Create canvas instead of main container
        self.canvas = ttk.Canvas(self, width=800, height=600)  # adjust size as needed
        self.canvas.pack(expand=True, fill="both")

        # Load and display background
        self.bg_image = Image.open("assets/images/casino_opening_screen.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Create the layout sections
        self.create_header()
        self.create_player_area()
        self.create_banker_area()
        self.create_result_area()
        self.create_controls()
        
        # Pack the main frame
        self.pack(expand=True, fill="both")

    def create_header(self):
        self.header = ttk.Label(self, text="Baccarat", font=("Times New Roman", 36, "bold"))
        self.canvas.create_window(512, 50, window=self.header)  # adjust x,y as needed

    def create_player_area(self):
        # Create LabelFrame with same styling
        self.player_box = ttk.LabelFrame(self, text="Player", padx=40, pady=20, width=1000, height=200)
                
        self.player_box.pack_propagate(False)  # Prevent resizing
        
        # Add message label inside the box (still using pack here since it's inside the frame)
        self.player_message = ttk.Label(self.player_box, text="No cards yet", font=("Arial", 18))
        self.player_message.pack(expand=True)
        
        # Place the entire LabelFrame on canvas
        self.canvas.create_window(512, 200, window=self.player_box)

    def create_banker_area(self):
        self.banker_box = ttk.LabelFrame(self, text="Banker", padx=20, pady=20, width=1000, height=200)
        self.banker_box.pack_propagate(False)
        
        self.banker_message = ttk.Label(self.banker_box, text="No cards yet", font=("Arial", 18))
        self.banker_message.pack(expand=True)

        self.canvas.create_window(512, 400, window=self.banker_box)

    def create_result_area(self):
        self.winner_box = ttk.LabelFrame(self, text="Winner", padx=20, pady=20, width=1000, height=200)
        self.winner_box.pack_propagate(False)
        
        self.winner_message = ttk.Label(self.winner_box, text="Game not started", font=("Arial", 18))
        self.winner_message.pack(expand=True)

        self.canvas.create_window(512, 550, window=self.winner_box)

    def create_controls(self):
        self.button_frame = ttk.Frame(self)
        
        self.continue_button = ttk.Button(self.button_frame, text="Continue", 
            font=("Arial", 14), 
            bg="#4CAF50",  # Green background
            fg="white",    # White text
            padx=20, 
            pady=10)
        self.continue_button.pack(side="left", padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Exit",
            font=("Arial", 14), 
            bg="#4CAF50",  # Green background
            fg="white",    # White text
            padx=20, 
            pady=10)
        self.exit_button.pack(side="right", padx=5)

        self.canvas.create_window(512, 700, window=self.button_frame)

        self.setup_exit_handling()

    def setup_exit_handling(self):
        self.master.bind('<Escape>', self.return_to_lobby)
        self.exit_button.config(command=self.return_to_lobby)

    def return_to_lobby(self):
        from screens.casino_lobby import CasinoLobby
        CasinoLobby(self.master, self.app_state)
        self.destroy()

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