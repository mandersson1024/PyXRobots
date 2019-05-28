
import tkinter as tk
import msvcrt


class Output:
    def __init__(self):
        pass

    def display(self, map_string: str) -> None:
        raise NotImplemented

    def hold(self) -> None:
        pass


class ConsoleOutput(Output):
    def __init__(self):
        super().__init__()

    def display(self, map_string: str) -> None:
        print()
        print(map_string)


class WindowOutput(Output):
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


def wait_for_keypress() -> str:
    while True:
        if msvcrt.kbhit():
            return msvcrt.getch().decode('ASCII')
