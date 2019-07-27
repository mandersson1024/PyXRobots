
import tkinter as tk


class WindowUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.bind('<Escape>', exit)
        self.label = tk.Label(self, font=("Courier", 16), padx=25, pady=25)

    def display(self, s: str) -> None:
        self.label.config(text=s)
        self.label.pack()
        self.update()

