
import tkinter as tk

rot = tk.Tk()
c = tk.Canvas(rot, width=640, height=640)
c.create_text(100, 100, text="Hello, World!")
c.grid()

rot.mainloop()

print("Hello, PyXRobots!")

