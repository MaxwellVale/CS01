# Maxwell Vale
# CS01 Section 1a
# Assignment 3

'''
lab3c.py
Simple L-system simulator.
'''

# References:
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/

import math

# ----------------------------------------------------------------------
# Example L-systems.
# ----------------------------------------------------------------------

# Koch snowflake.
koch = { 'start' : 'F++F++F',
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1',
              '+' : 'R 60',
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A',
             'A'     : '-BF+AFA+FB-' ,
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1',
                 '-' : 'L 90',
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G',
               'F'     : 'F-G+F+G-F',
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1',
                    'G' : 'F 1',
                    '+' : 'L 120',
                    '-' : 'R 120' }

# ----------------------------------------------------------------------
# L-systems functions.
# ----------------------------------------------------------------------

def update(LDict, LString):
    updated = ''
    for char in LString:
        if char in LDict:
            updated += LDict[char]
        else:
            updated += char
    return updated


def iterate(lsys, n):
    '''<docstring>'''
    LString = lsys['start']
    for i in range(n):
        LString = update(lsys, LString)
    return LString


def lsystemToDrawingCommands(draw, s):
    '''<docstring>'''
    commands = []
    for char in s:
        if char in draw:
            commands.append(draw[char])
    return commands


def bounds(cmds):
    '''<docstring>'''
    x = 0
    y = 0
    angle = 0
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for cmd in cmds:
        x = nextLocation(x, y, angle, cmd)[0]
        y = nextLocation(x, y, angle, cmd)[1]
        angle = nextLocation(x, y, angle, cmd)[2]
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y
    return (float(xmin), float(xmax), float(ymin), float(ymax))

def nextLocation(x, y, angle, cmd):
    '''<docstring>'''
    command = cmd.split()
    if command[0] == 'F':
        x += math.cos(angle * math.pi / 180)
        y += math.sin(angle * math.pi / 180)
        return (float(x), float(y), angle)
    else:
        if command[0] == 'R':
            angle -= int(command[1])
        else:
            angle += int(command[1])
        return (float(x), float(y), angle % 360)

def saveDrawing(filename, bounds, cmds):
    '''<docstring>'''
    f = open(filename, 'w')
    for b in bounds:
        f.write(str(b) + ' ')
    f.write('\n')
    for cmd in cmds:
        f.write(cmd + '\n')
    f.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
