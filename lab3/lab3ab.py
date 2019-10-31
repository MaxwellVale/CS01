# Maxwell Vale
# CS01 Section 1a
# Assignment 3

import math

# Part A: Exercises
# Ex A.1
def list_reverse(lst):
    copy = lst.copy()
    copy.reverse()
    return copy

# Ex A.2
def list_reverse2(lst):
    copy = []
    for index in range(len(lst) - 1, -1, -1):
        copy.append(lst[index])
    return copy

# Ex A.3
def file_info(fileName):
    f = open(fileName, 'r')
    lines = 0
    words = 0
    chars = 0
    line = f.readline() # get rid of this ugliness please

    while line != '':
        lines += 1
        words += len(line.split())
        chars += len(line)
        line = f.readline()
    f.close()
    return (lines, words, chars)

# Ex A.4
def file_info2(fileName):
    lwc = file_info(fileName)
    d = {"lines" : lwc[0],
         "words" : lwc[1],
         "characters" : lwc[2]}
    return d

# Ex A.5
def longest_line(fileName):
    f = open(fileName, 'r')
    longest = f.readline()
    line = ' '

    while line != '':
        if len(line) > len(longest):
            longest = line
        line = f.readline()
    f.close()
    return (len(longest), longest)

# Ex A.6
def sort_words(str):
    sorted = str.split()
    sorted.sort()
    return sorted

# Ex A.7
# 11011010 binary to decimal
# Every position with a one is a 2 to that index (starting from the right)
# 2 + 8 + 16 + 64 + 128 = 218
# The largest 8 digit binary number would be 11111111, which in decimal is 255

# Ex A.8
def binaryToDecimal(binList):
    copy = binList.copy()
    copy.reverse()
    dec = 0

    for index in range(len(copy)):
        dec += copy[index] * 2 ** index
    return dec

# Ex A.9
def decimalToBinary(n):
    if n == 0:
        return [0]

    else:
        num = n
        lenBin = int(math.log(n, 2) + 1)
        binList = []

        for index in range(lenBin):
            if num >= 2 ** (lenBin - 1 - index):
                binList.append(1)
                num -= 2 ** (lenBin - 1 - index)
            else:
                binList.append(0)
        return binList

# Part B: Pitfall: Poor coding style

# Ex B.2.1
# def sc(a,b,c):
#     return a*a*a+b*b*b+c*c*c
# Style Errors: [OPERATOR_SPACE], [COMMA_SPACE], [BAD_NAMES]
def sumCubes(a, b, c):
    return a * a * a + b * b * b + c * c * c

# Ex B.2.2
# This example was way too long to fit in here
# Style Errors: [BAD_NAMES], [LINE_LENGTH], [COMMENT_SPACE], [COMMENT_GRAMMATICAL]
def sumOfCubes(a, b, c, d):
    # Return sum of cubes of arguments a, b, c, and d.
    return a * a * a + b * b * b + c * c * c + d * d * d

# Ex B.2.3
# def sum_of_squares(x, y):
#        return x * x + y * y
# def sum_of_three_cubes(x, y, z):
#    return x * x * x + y * y * y + z * z * z
# Style Errors: [BLANK_LINES], [INDENT_CONSISTENT]
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z
