# Maxwell Vale
# CS01 Section 1a
# Assignment 4

from tkinter import *

# Setup
root = Tk()
root.geometry('800x800')
c = Canvas(root, width=800, height=800)
c.pack()

# Drawing the four rectangles
rectRed = c.create_rectangle(0, 0, 100, 100, fill='red', outline='red')
rectGreen = c.create_rectangle(800, 0, 700, 100, fill='green', outline='green')
rectBlue = c.create_rectangle(0, 800, 100, 700, fill='blue', outline='blue')
rectYellow = c.create_rectangle(800, 800, 700, 700, fill='yellow', outline='yellow')

root.mainloop()
