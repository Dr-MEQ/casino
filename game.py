# Game management logic for Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk

from display import Display
from deck import Deck

class Game():
    def __init__(self):
        self.display = Display()
        self.deck = Deck()
        self.player_hand = []
        self.banker_hand = []

    def start_game(self):
        # Show initial display
        self.show_dealing_message()
        self.after(3000, self.deal_initial_cards)  # After 3 seconds, deal cards
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
        player_hand = [self.deck.draw(), self.deck.draw()]
        banker_hand = [self.deck.draw(), self.deck.draw()]

        # Update displays
        self.player_message.config(text=f"Player's cards: {player_hand[0]}")
        self.banker_message.config(text="Dealer's card: Hidden")

        player_value = self.hand_value(player_hand)
        #print(f"Player has a {player_value}")
              
        if player_value <= 5:
            player_hand.append(self.deck.draw())
            print(f"Player draws: {player_hand[-1]}")
            time.sleep(1)
            player_value = self.hand_value(player_hand)
            print(f"Player now has a {player_value}")
            time.sleep(1)

        print(f"Banker's hand: {banker_hand} - Value: {self.hand_value(banker_hand)}")
        time.sleep(1)
        
        banker_value = self.hand_value(banker_hand)
        if banker_value <= 5:
            banker_hand.append(self.deck.draw())
            print(f"Banker draws: {banker_hand[-1]}")
            time.sleep(1)
            banker_value = self.hand_value(banker_hand)

        if player_value > banker_value:
            print("Player wins!")
        elif banker_value > player_value:
            print("Banker wins!")
        else:
            print("It's a tie!")