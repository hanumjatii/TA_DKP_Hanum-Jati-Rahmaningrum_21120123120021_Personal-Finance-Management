from customtkinter import *

class Page:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.frame = CTkFrame(parent)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()