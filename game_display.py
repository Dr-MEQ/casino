# Display management for Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk
from display import BaseDisplay
from titlescreen import TitleScreen
from game import Game
from card import Card

class GameDisplay(BaseDisplay):
    def __init__(self, master, game_state):
        super().__init__(master)
        self.game_state = game_state
        self.master.title("Baccarat Game")

        # Header at top
        self.header = tk.Label(self.main_container, text="Baccarat", font=("Arial", 24))
        self.header.pack(pady=(0, 30))
        
        # Player box in upper third
        self.player_box = tk.LabelFrame(self.main_container, text="Player", padx=20, pady=20)
        self.player_box.pack(fill="both", expand=True, pady=(0, 30))
        self.player_message = tk.Label(self.player_box, text="", font=("Arial", 18))
        self.player_message.pack(expand=True)

        # Banker box in middle third
        self.banker_box = tk.LabelFrame(self.main_container, text="Banker", padx=20, pady=20)
        self.banker_box.pack(fill="both", expand=True, pady=(0, 30))
        self.banker_message = tk.Label(self.banker_box, text="", font=("Arial", 18))
        self.banker_message.pack(expand=True)

        # Winner box in lower third
        self.winner_box = tk.LabelFrame(self.main_container, text="Winner", padx=20, pady=20)
        self.winner_box.pack(fill="both", expand=True)
        self.winner_message = tk.Label(self.winner_box, text="", font=("Arial", 18))
        self.winner_message.pack(expand=True)

        # Control buttons at the bottom
        self.button_frame = tk.Frame(self.main_container)
        self.button_frame.pack(fill="x", pady=(20, 0))
    
        self.continue_button = tk.Button(self.button_frame, text="Continue")
        self.continue_button.pack(side="left", padx=5)
    
        self.exit_button = tk.Button(self.button_frame, text="Exit")
        self.exit_button.pack(side="right", padx=5)

        # Pack the main frame itself!
        self.pack(expand=True, fill="both")

        # Setup exit handling
        self.setup_exit_handling()

    def setup_exit_handling(self):
        # Bind Escape key
        self.master.bind('<Escape>', self.return_to_title)
        # Bind exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.return_to_title)
        self.exit_button.pack(side="right", padx=5)

    def return_to_title(self, event=None):
        # Clean up current game state
        self.game_state.clear()

        # Hide/destroy GameDisplay
        self.master.destroy()

        # Show TitleScreen again
        title_screen = TitleScreen(self.master)

    #def update_game_state(self, state_data):
        # Call parent's update method first
        #super().update_game_state(state_data)

        """Updates all display elements based on current game state"""
        #if 'window_title' in state_data:
        #    self.master.title(state_data['window_title'])
        #if 'message' in state_data:
        #    self.message_label.config(text=state_data['message'])
        #if 'player_message' in state_data:
        #    self.player_message.config(text=state_data['player_message'])
        #if 'banker_message' in state_data:
        #    self.banker_message.config(text=state_data['banker_message'])
        #if 'winner_message' in state_data:
        #    self.winner_message.config(text=state_data['winner_message'])

   