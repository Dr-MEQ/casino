# Card operations for the Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"