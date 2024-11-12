# Game management logic for Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk

from display import Display
from deck import Deck

class Game():
    def __init__(self, display):
        self.display = display
        self.deck = Deck()
        self.player_hand = []
        self.banker_hand = []
        self.show_initial_screen()

    def show_initial_screen(self):        
        self.display.update_game_state({'message': 'Welcome to Baccarat!'})
        
        # Create button frame at bottom with start and exit buttons
        button_frame = tk.Frame(self.display)
        start_button = tk.Button(button_frame, text="Start Game", command=self.start_game)
        exit_button = tk.Button(button_frame, text="Exit", command=self.display.quit)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        start_button.pack(side=tk.LEFT)
        exit_button.pack(side=tk.RIGHT)

        
        # Bind keys
        self.display.focus_set()  # or focus_force() if needed
        self.display.bind('<space>', lambda event: self.start_game())
        self.display.bind('<Escape>', lambda event: self.quit())
    
    def start_game(self):
        # Show initial display
        self.display.show_dealing_message()
        self.display.after(3000, self.deal_initial_cards)  # After 3 seconds, deal cards
        self.play()
        self.display.mainloop()

    def card_value(self, card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 0
        elif card.rank == 'Ace':
            return 1
        else:
            return int(card.rank)

    def hand_value(self, hand):
        return sum(self.card_value(card) for card in hand) % 10

    def play(self):
        self.player_hand = [self.deck.draw(), self.deck.draw()]
        self.banker_hand = [self.deck.draw(), self.deck.draw()]

        # Initial display update
        self.display.update_player_hand(self.player_hand)
        self.display.update_banker_hand(["Hidden", self.banker_hand[1]])  # Show one card

        player_value = self.hand_value(self.player_hand)
        
        # Use after() for delays instead of time.sleep()
        if player_value <= 5:
            def draw_player_card():
                self.player_hand.append(self.deck.draw())
                self.display.update_player_hand(self.player_hand)
                self.display.update_message(f"Player draws: {self.player_hand[-1]}")
                self.handle_banker_turn()
                
            self.display.after(1000, draw_player_card)
        else:
            self.handle_banker_turn()

    def handle_banker_turn(self):
        banker_value = self.hand_value(self.banker_hand)
        self.display.update_banker_hand(self.banker_hand)  # Show all cards
        
        if banker_value <= 5:
            def draw_banker_card():
                self.banker_hand.append(self.deck.draw())
                self.display.update_banker_hand(self.banker_hand)
                self.display.update_message(f"Banker draws: {self.banker_hand[-1]}")
                self.show_result()
                
            self.display.after(1000, draw_banker_card)
        else:
            self.show_result()

    def show_result(self):
        player_value = self.hand_value(self.player_hand)
        banker_value = self.hand_value(self.banker_hand)

    def deal_cards(self):
        state = {
            'player_message': 'Dealing...',
            'banker_message': 'Dealing...',
            'result_message': 'Dealing...'
        }
        self.display.update_game_state(state)

    def show_dealing_message(self, player_first_card=None):
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

    def update_player_hand(self, hand):
        hand_text = ", ".join(str(card) for card in hand)
        self.player_message.config(text=f"Player's hand: {hand_text}")

    def update_banker_hand(self, hand):
        hand_text = ", ".join(str(card) for card in hand)
        self.banker_message.config(text=f"Banker's hand: {hand_text}")

    def update_message(self, message):
        self.winner_message.config(text=message) 

    def quit(self):
        self.display.quit()  # or however you access the root window  