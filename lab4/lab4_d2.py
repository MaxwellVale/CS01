# Maxwell Vale
# CS01 Section 1a
# Assignment 4

from tkinter import *

def draw_square(canvas, color, sideLen, center):
    '''docstring'''
    return canvas.create_rectangle(center[0] - sideLen / 2, center[1] - sideLen / 2, \
                                   center[0] + sideLen / 2, center[1] + sideLen / 2, \
                                   fill=color, outline=color)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    c.pack()

    draw_square(c, 'red', 100, (50, 50))
    draw_square(c, 'green', 100, (750, 50))
    draw_square(c, 'blue', 100, (50, 750))
    draw_square(c, 'yellow', 100, (750, 750))

    root.mainloop()
