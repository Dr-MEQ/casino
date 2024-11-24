# Main flow of the casino application
import tkinter as tk
import ttkbootstrap as ttk
from screens.casino_entrance import CasinoEntrance
from state.game_state import GameState

# Function to position window on top right of second monitor

def position_top_right_second_monitor(window):
    # print(f"Initial window size: {window.winfo_width()}x{window.winfo_height()}")
    window.update_idletasks()
    # print(f"After update_idletasks: {window.winfo_width()}x{window.winfo_height()}")
    
    window.attributes('-alpha', 0.0)  # Make window transparent

    window.update()
    window.update_idletasks()
    
    # Get window dimensions
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Add a minimum size check
    if window_width < 100 or window_height < 100:  # adjust these values based on your expected window size
        print(f"Warning: Window dimensions seem too small: {window_width}x{window_height}")
        # Maybe wait a bit and try again, or use default sizes
        window_width = max(window_width, 1600)  # default minimum width
        window_height = max(window_height, 1200)  # default minimum height
        window.geometry(f"{window_width}x{window_height}")
        
    # Calculate position
    x = 3840 - window_width - 40
    y = 20

    # Screen boundary check
    screen_width = window.winfo_screenwidth()
    if x < 0 or x > screen_width:
        print(f"Warning: Window x position ({x}) outside screen bounds")
        x = max(0, min(x, screen_width - window_width))
    
    # Position the window
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    
    # Force another update to ensure changes take effect
    window.update()
    window.attributes('-alpha', 1.0)  # Make window visible

    # print(f"Final window position: {x},{y}")
    # print(f"Final window size: {window_width}x{window_height}")
   

class MainApplication:
    def __init__(self, root):
        # Initialize ALL instance variables first
        self.root = root
        self.screens_opened = 0  # Initialize counter
        self.current_screen = None  # Initialize screen reference
        self.game_state = {}  # Initialize game state
        self.game_state = GameState().get_state()
        
        self.is_closing = False  # Initialize closing flag
        
        # AFTER all initialization, show the first screen
        self.show_casino_entrance()

    def show_casino_entrance(self):  # This needs to be indented under MainApplication

        #print("Entering show_casino_entrance method")  # Debug print
        #print("Object attributes:", vars(self))  # Debug print
        
        self.root.after(100, self._create_casino_entrance)  # Call the method after 100ms

    def _create_casino_entrance(self):  # This needs to be indented under MainApplication

        if hasattr(self, 'current_screen') and self.current_screen is not None:
            self.current_screen.destroy()
        
        #self.screens_opened += 1
        #print(f"Opening screen #{self.screens_opened}")
        self.current_screen = CasinoEntrance(self.root, self.game_state)
        
def main():
    root = ttk.Window(themename="darkly")
    root.geometry("1600x1200")
    app = MainApplication(root)
    position_top_right_second_monitor(root)
    root.mainloop()

if __name__ == "__main__":
    main()