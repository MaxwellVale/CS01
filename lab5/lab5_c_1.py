# Maxwell Vale
# CS01 Section 1a
# Assignment 5

from tkinter import *
import random

# Graphics commands.

def random_color():
    '''
    Function random_color
    Generates random colors of the form #RRGGBB

    Arguments
    No arguments

    Return
    Returns a random color as a string in the form "#RRGGBB", where
    each character in "RRGGBB" is a hexadecimal digit.
    '''
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    c = '#'
    for i in range(6):
        c += str(random.choice(hex))
    return c

def draw_circle(x, y, r, color):
    '''
    Function draw_circle
    Draws a circle given its center point, radius, and color.

    Arguments
    x, y --> The coordinates of the center of the circle being drawn.
    r --> The radius of the circle.
    color --> The outline and fill color of the circle in the form "#RRGGBB"

    Return
    Returns the handle of the drawn circle.
    '''
    circle = canvas.create_oval(x - r, y - r, x + r, y + r,
                                outline=color, fill=color)
    return circle

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global circles
    global color
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for circle in circles:
            canvas.delete(circle)
        circles = []

def button_handler(event):
    '''Handle left mouse button click events.'''
    diameter = random.randint(10, 50)
    circle = draw_circle(event.x, event.y, diameter / 2, color)
    circles.append(circle)


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    color = random_color()
    circles = []

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
