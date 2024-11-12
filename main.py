#import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from screens.casino_entrance import CasinoEntrance
from state.game_state import GameState

def position_top_right_second_monitor(window):
    # First, make sure the window is fully created and sized
    window.update_idletasks()
    
    # Get window dimensions
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    
    # Debug prints
    print(f"Window dimensions: {window_width}x{window_height}")
    print(f"Screen width: {window.winfo_screenwidth()}")
    
    # Calculate position (still using your values for now)
    x = 3840 - window_width - 50
    y = 20
    
    print(f"Setting position to: +{x}+{y}")
    window.geometry(f"+{x}+{y}")

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino")
        self.current_screen = None
        self.game_state = GameState()
        self.show_casino_entrance()
        
    def show_casino_entrance(self):
        self.current_screen = CasinoEntrance(self.root, self.game_state)

def main():
    root = ttk.Window(themename="darkly")

    # Add a protocol handler for window close button
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    # Add keyboard shortcut to quit
    root.bind('<Escape>', lambda e: root.quit())

    frame = ttk.Frame(root, bootstyle="dark")
    app = MainApplication(root)

    root.update()  # Make sure window size is calculated
    position_top_right_second_monitor(root)
    root.mainloop()

if __name__ == "__main__":
    main()