
import tkinter as tk


class WindowUI(tk.Tk):
    def __init__(self, keypress_callback: callable):
        super().__init__()

        def on_key_release(event) -> None:
            keypress_callback(event.char)

        self.bind("<KeyRelease>", on_key_release)
        self.label = tk.Label(self, font=("Courier", 16), padx=25, pady=25)

    def display(self, s: str) -> None:
        self.label.config(text=s)
        self.label.pack()
        self.update()

