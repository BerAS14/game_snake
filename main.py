import time
import tkinter
from tkinter import *

x1, y1, x2, y2 = 10, 10, 100, 10
window = tkinter.Tk()
canva = tkinter.Canvas(window, width=500, height=500, bg="grey")
canva.focus_set()
canva.pack()

line = canva.create_line(x1, y1, x2, y2, width=5, fill="blue")
canva.move(line, 100, 0)

canva.pack()
mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
