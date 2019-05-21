
import tkinter as tk

class UI:
    def __init__(self):
        pass

    def display(self, map_string: str) -> None:
        raise NotImplemented

    def hold(self) -> None:
        pass


class ConsoleUI(UI):
    def __init__(self):
        super().__init__()

    def display(self, map_string: str) -> None:
        print(map_string)


class WindowUI(UI):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.text_field = tk.Text(self.root)
        self.text_field.grid()

    def display(self, s: str) -> None:
        self.text_field.insert(tk.INSERT, s)
        self.text_field.grid()
        self.root.update()

    def hold(self) -> None:
        self.root.mainloop()



