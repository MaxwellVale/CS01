# Maxwell Vale
# CS01 Section 1a
# Assignment 4

import random
import nose

# Part B: Exercises

# Ex B.1
def random_size(a, b):
    '''
    Function random_size
    Takes two non-negative integers and returns a random even integer
    which is between the two arguments. Uses the randint function from
    the random module.

    Arguments
    a, b --> Both non-negative even integers and a < b.

    Return
    Returns a random even integer which is >= a and <= b.
    '''
    assert (a >= 0 and b >= 0), "Arguments should be non-negative."
    assert (a % 2 == 0 and b % 2 == 0), "Arguments should be even."
    assert (a < b), "First argument must be smaller than the second."
    num = random.randint(a, b)
    # If the number isn't even, then add or subtract 1 from the number.
    if num % 2 != 0:
        num += random.choice([-1, 1])
    assert (num % 2 == 0), "Output should be even."
    return num

# Ex B.2
def random_position(max_x, max_y):
    '''
    Function random_position
    Takes two non-negative integers representing a maximum x and y coordinate
    and gives a tuple of a random coordinate pair (in pixels).

    Arguments
    max_x, max_y --> Both non-negative integers

    Return
    Returns a random (x, y) pair as a tuple such that 0 <= x <= max_x and
    0 <= y <= max_y.
    '''
    assert (max_x >= 0 and max_y >= 0), "Arguments should be non-negative."
    return (random.randint(0, max_x), random.randint(0, max_y))

# Ex B.3
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

# Ex B.4
def count_values(dict):
    '''
    Function count_values
    Counts the number of unique values in dict.

    Arguments
    dict --> A dictionary

    Return
    Returns an integer representing the number of unique values
    in dict.
    '''
    return len(set(dict.values()))

# Ex B.5
def remove_value(dict, value):
    '''
    Function remove_value
    Removes all entries in dict with argument "value" as its value.
    If there is no such "value" in dict, then the function does nothing.

    Arguments
    dict --> A dictionary
    value --> An arbitrary item which may or may not be a value in dict.

    Return
    Function does not return anything.
    '''
    keys = list(dict.keys())
    removals = []
    for key in keys:
        if dict[key] == value:
            removals.append(key)
    for k in range(len(removals)):
        del dict[removals[k]]

# Ex B.6
def split_dict(dict):
    '''
    Function split_dict
    Takes a dictionary and splits it based on the order of the keys in
    the alphabet. If the keys start with the letters a-m, then they go
    into the first dictionary. Keys that start with letters n-z go into
    the second dictionary. Keys retain their values from the original
    dictionary.

    Arguments
    dict --> Dictionary which uses strings as keys.

    Return
    Returns a tuple of two dictionaries with key/value pairs from the
    original dictionary. The first dictionary in the tuple contains pairs
    whose keys start with the letters a-m, while the other dictionary has
    pairs with keys that start with the letters n-z.
    '''
    aTom = {} # Dictionary with keys starting with letters a-m
    nToz = {} # Dictionary with keys starting with letters n-z
    keys = list(dict.keys())
    for key in keys:
        if key.lower() < 'n':
            aTom[key] = dict[key]
        else:
            nToz[key] = dict[key]
    return (aTom, nToz)

# Ex B.7
def count_duplicates(dict):
    '''
    Function count_duplicates
    Counts the number of duplicate values in the dictionary.

    Arguments
    dict --> A dictionary.

    Return
    Returns the number of duplicate values in dict.
    '''
    duplicates = set()
    values = list(dict.values())
    for value in values:
        if values.count(value) >= 2:
            duplicates.add(value)
    return len(duplicates)
