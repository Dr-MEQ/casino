# Display management for Baccarat game

import random, time, os
import sys
from typing import List
import tkinter as tk

from card import Card

class BaseDisplay(tk.Frame):
    def __init__(self, master, app_name="Baccarat"):
        super().__init__(master)
        self.master = master
        self.master.title(app_name)
        self.master.geometry("900x1200")
        
        # Create a main container frame
        self.main_container = tk.Frame(self)
        self.main_container.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Pack the main frame itself
        self.pack(expand=True, fill="both")

