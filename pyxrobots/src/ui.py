
import tkinter as tk


class WindowUI(tk.Tk):
    width: int
    height: int

    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 22
        self.bind('<Escape>', exit)
        self.label = tk.Label(self, font=("Courier", 16), padx=25, pady=25)

    def display(self, s: str) -> None:
        self.label.config(text=s)
        self.label.pack()
        self.update()

    def bind_key(self, key: str, func: callable) -> None:
        def on_key(_) -> None:
            func()
        self.bind(key, on_key)

    def unbind_key(self, key: str) -> None:
        self.unbind(key)

