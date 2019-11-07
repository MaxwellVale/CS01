# Maxwell Vale
# CS01 Section 1a
# Assignment 4

from tkinter import *

def draw_square(canvas, color, sideLen, center):
    '''
    Function draw_square
    Draws a square on canvas of size sideLen, centered at center,
    and filled with color.

    Arguments
    canvas --> The canvas on which the square will be drawn.
    color --> The fill and outline color of the square.
    sideLen --> The side length of the square in pixels.
    center --> The position of the center of the square. Represented as a
    tuple in the form (x, y), representing the horizontal and vertical position
    of the center.

    Return
    Returns the handle of the square that was drawn on the canvas.
    '''
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
