import random, time, os
import sys
from typing import List
import tkinter as tk
from PIL import Image, ImageTk  # For handling the image
from display import Display

class TitleScreen:
    def __init__(self, display):
        self.display = display
        self.window = display.window
        self.canvas = display.canvas  # Use Display's canvas
        self.width = display.width
        self.height = display.height
        self.prompt_objects = []
        self.prompt_visible = True

         # Load background image
        self.bg_image = Image.open("casino_opening_screen.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
       
        self.setup_title_screen()

    def setup_title_screen(self):
        
        # Clear any existing content
        self.canvas.delete("all")

        # Add background
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Set window size to match image
        self.master.geometry(f"{self.width}x{self.height}")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Configure the frame to expand
        self.pack(fill="both", expand=True)
        
        # Create canvas with explicit dimensions
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        
        # Add background
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # "CASINO" with thicker shadow
        offsets = [(2,2), (2,-2), (-2,2), (-2,-2)]  # diagonal offsets
        for offset_x, offset_y in offsets:
            self.canvas.create_text(width/2+offset_x, height/4+offset_y,
                                  text="CASINO", 
                                  font=("Arial", 72, "bold"),
                                  fill="black")
        self.canvas.create_text(width/2, height/4,
                              text="CASINO", 
                              font=("Arial", 72, "bold"),
                              fill="gold")
        
        # "BACCARAT" with thicker shadow
        for offset_x, offset_y in offsets:
            self.canvas.create_text(width/2+offset_x, height*3/5+offset_y,
                                  text="BACCARAT", 
                                  font=("Arial", 86, "bold"),
                                  fill="black")
        self.canvas.create_text(width/2, height*3/5,
                              text="BACCARAT", 
                              font=("Arial", 86, "bold"),
                              fill="gold")
        
        # Create shadow layers for the prompt
        prompt_text = "Press any key to start"
        prompt_x = width/2
        prompt_y = height*0.9
        
        # Store all the text objects (shadows and main text)
        self.prompt_objects = []

        self.pack()
        
        # Create shadow layers
        offsets = [(2,2), (2,-2), (-2,2), (-2,-2)]
        for offset_x, offset_y in offsets:
            shadow = self.canvas.create_text(
                prompt_x + offset_x, prompt_y + offset_y,
                text=prompt_text,
                font=("Arial", 36, "bold"),
                fill="black"
            )
            self.prompt_objects.append(shadow)
        
        # Create main text
        self.prompt = self.canvas.create_text(
            prompt_x, prompt_y,
            text=prompt_text,
            font=("Arial", 36, "bold"),
            fill="red"
        )
        self.prompt_objects.append(self.prompt)

        # Initialize the flash state
        self.prompt_visible = True
        
        # Bind keyboard event and set focus
        self.canvas.bind('<Key>', self.on_keypress)
        self.canvas.bind('<Button>', self.on_keypress)      # Any mouse button
        self.canvas.focus_set()
        
        # Start the flashing animation
        self.flash_prompt()
        
    def flash_prompt(self):
        # Hide/show all prompt objects (shadows and main text)
        state = 'hidden' if self.prompt_visible else 'normal'
        for text_obj in self.prompt_objects:
            self.canvas.itemconfig(text_obj, state=state)
        self.prompt_visible = not self.prompt_visible
        self.after(500, self.flash_prompt)
    
    def on_keypress(self, event):
        self.destroy()
        return

    
    def destroy_screen(self):
        self.destroy()
        return