# Maxwell Vale
# CS01 Section 1a
# Assignment 5

from tkinter import *
import random
import math

# Graphics commands.

def random_color():
    '''
    Function random_color
    Generates random colors of the form #RRGGBB

    Arguments
    No arguments

    Return
    Returns a random color as a string in the form ""#RRGGBB", where
    each character in "RRGGBB" is a hexadecimal digit.
    '''
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    c = '#'
    for i in range(6):
        c += str(random.choice(hex))
    return c

def draw_line(x1, y1, x2, y2, color):
    '''
    Function draw_line
    Draws a line on the canvas given the endpoints of the line and the color.
    Setting a default width of two.

    Arguments
    x1, y1 --> Coordinates of the first endpoint of the line.
    x2, y2 --> Coordinates of the second endpoint of the line.
    color --> The color of the line in the form "#RRGGBB".

    Return
    Returns the handle of the line being drawn.
    '''
    line = canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
    return line

def draw_star(x, y, r, color):
    '''
    Function draw_star
    Draws a star centered at (x, y) and circumscribed by a circle of radius r.
    Uses the draw_line function to connect a set of points.

    Arguments
    x, y --> Coordinates of the center of the star.
    r --> Radius of the circle circumscribing the star.
    color --> The color of the star in the form "#RRGGBB".

    Return
    Does not return anything.
    '''
    global lines
    # Since the star needs to point upwards, the first point should be directly
    # above the center of the star (hence the x coordinate remains the same).
    points = [(x, y - r)]
    for i in range(1, n):
        # Adding a multiple of 2 * pi / n with every iteration.
        # Need to add math.pi / 2 because our first point is (x, y - r)
        points.append((x + r * math.cos(math.pi / 2 + i * 2 * math.pi / n),
                       y - r * math.sin(math.pi / 2 + i * 2 * math.pi / n)))
    for i in range(n):
        x1 = points[i][0]
        y1 = points[i][1]
        # The connected points should be as far apart as possible.
        # This can be achieved by going (n - 1) / 2 down the list.
        x2 = points[int((i + (n - 1) / 2) % n)][0]
        y2 = points[int((i + (n - 1) / 2) % n)][1]
        line = draw_line(x1, y1, x2, y2, color)
        lines.append(line)

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global lines
    global color
    global n
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for line in lines:
            canvas.delete(line)
        lines = []
    elif key == 'plus':
        n += 2
    elif key == 'minus' and n > 5:
        n -= 2

def button_handler(event):
    '''Handle left mouse button click events.'''
    r = random.randint(50, 100)
    draw_star(event.x, event.y, r, color)


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    n = 5
    lines = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
