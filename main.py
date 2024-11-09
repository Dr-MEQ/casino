import random, time, os
import sys
from typing import List
import tkinter as tk
from PIL import Image, ImageTk  # For handling the image
import tkinter.messagebox
from titlescreen import TitleScreen
from game import Game

def main():
    root = tk.Tk()
    title = TitleScreen(root)
    
    root.mainloop()  # Add this line

    #game = Game()
    #while not game.is_over():
    #    game.play_round()
    #game.show_results()

if __name__ == "__main__":
    main()

