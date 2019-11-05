# Maxwell Vale
# CS01 Section 1a
# Assignment 4

import random
import nose

# Part B: Exercises

# Ex B.1
def random_size(a, b):
    '''docstring'''
    assert (a >= 0 and b >= 0), "Arguments should be non-negative."
    assert (a % 2 == 0 and b % 2 == 0), "Arguments should be even."
    assert (a < b), "First argument must be smaller than the second."
    num = random.randint(a, b)
    if num % 2 != 0:
        num += random.choice([-1, 1])
    assert (num % 2 == 0), "Output should be even."
    return num

# Ex B.2
def random_position(max_x, max_y):
    '''docstring'''
    assert (max_x >= 0 and max_y >= 0), "Arguments should be non-negative."
    return (random.randint(0, max_x), random.randint(0, max_y))

# Ex B.3
def random_color():
    '''docstring'''
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    c = '#'
    for i in range(6):
        c += str(random.choice(hex))
    return c

# Ex B.4
def count_values(dict):
    '''docstring'''
    return len(set(dict.values()))

# Ex B.5
def remove_value(dict, value):
    '''docstring'''
    keys = list(dict.keys())
    removals = []
    for key in keys:
        if dict[key] == value:
            removals.append(key)
    for k in range(len(removals)):
        del dict[removals[k]]

# Ex B.6
def split_dict(dict):
    '''docstring'''
    aTom = {}
    nToz = {}
    keys = list(dict.keys())
    for key in keys:
        if key.lower() < 'n':
            aTom[key] = dict[key]
        else:
            nToz[key] = dict[key]
    return (aTom, nToz)

# Ex B.7
def count_duplicates(dict):
    '''docstring'''
    duplicates = set()
    values = list(dict.values())
    for value in values:
        if values.count(value) >= 2:
            duplicates.add(value)
    return len(duplicates)
