# Display management for Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk

from card import Card

class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Baccarat Game")
        self.geometry("900x1200")
        self.message_label = tk.Label(self, text="", font=("Arial", 24))
        self.message_label.pack(pady=20)

        # Player Box
        self.player_box = tk.LabelFrame(self, text="Player", padx=10, pady=10)
        self.player_box.pack(padx=10, pady=10, fill="both", expand=True)
        

        # Banker Box
        self.banker_box = tk.LabelFrame(self, text="Banker", padx=10, pady=10)
        self.banker_box.pack(padx=10, pady=10, fill="both", expand=True)

        # Winner Box
        self.winner_box = tk.LabelFrame(self, text="Winner", padx=10, pady=10)
        self.winner_box.pack(padx=10, pady=10, fill="both", expand=True)

    def show_dealing_message(self):
        self.player_message = tk.Label(self.player_box, text="Dealing...", font=("Arial", 18), fg="blue")
        self.banker_message = tk.Label(self.banker_box, text="Dealing...", font=("Arial", 18), fg="red")
        self.winner_message = tk.Label(self.winner_box, text="Dealing...", font=("Arial", 18), fg="green")
        # Pack each message separately
        self.player_message.pack(padx=10, pady=10)
        self.banker_message.pack(padx=10, pady=10)
        self.winner_message.pack(padx=10, pady=10)

        flash_count = 0
        def flash():
            nonlocal flash_count
            current_text = self.player_message.cget("text")
            new_text = "" if current_text == "Dealing..." else "Dealing..."
            
            self.player_message.config(text=new_text)
            self.banker_message.config(text=new_text)
            self.winner_message.config(text=new_text)

            flash_count += 1 
            if flash_count < 6:
                self.after(500, flash)
            else:           
                # After 3 seconds, update with initial cards
                self.player_message.config(text=f"Player's first card: {player_first_card}")
                self.banker_message.config(text="Dealer's card: Hidden")
                self.after(500, lambda: self.flash_winner_only())
            
    
        flash()  # Start the flashing
    
    def flash_winner_only(self):
        current_text = self.winner_message.cget("text")
        new_text = "" if current_text == "Dealing..." else "Dealing..."