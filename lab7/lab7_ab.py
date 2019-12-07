# Maxwell Vale
# CS01 Section 1a
# Assignment 7

# Part A: Exercises
# Ex A.1.1
def union(s1, s2):
    u = set(s1)
    for item in s2:
        u.add(item)
    return u

# Ex A.1.2
def intersection(s1, s2):
    i = set()
    for item in s1:
        if item in s2:
            i.add(item)
    return i

# Ex A.1.3
def difference(s1, s2):
    d = set()
    i = intersection(s1, s2)
    for item in s1:
        if item not in i:
            d.add(item)
    return d

# Ex A.2
def mySum(*nums):
    sum = 0
    if len(nums) == 0:
        return sum
    for n in nums:
        if type(n) is not int:
            raise TypeError("Arguments must be positive integers.")
        elif n < 1:
            raise ValueError("Arguments must be positive integers.")
        else:
            sum += n
    return sum

# Ex A.3
def myNewSum(*nums):
    sum = 0
    if len(nums) == 0:
        return sum
    elif len(nums) == 1 and type(nums[0]) is list:
        for num in nums[0]:
            if type(num) is not int:
                raise TypeError("Elements in list must be positive integers.")
            elif num < 1:
                raise ValueError("Elements in list must be positive integers.")
            else:
                sum += num
        return sum
    else:
        for n in nums:
            if type(n) is not int:
                raise TypeError("Arguments must be positive integers.")
            elif n < 1:
                raise ValueError("Arguments must be positive integers.")
            else:
                sum += n
        return sum

# Ex A.4
def myOpReduce(intList, **kwargs):
    if len(kwargs) == 0:
        raise ValueError("No keyword argument.")
    elif len(kwargs) > 1:
        raise ValueError("Too many keyword arguments.")
    else:
        arg, op = list(kwargs.items())[0]
        if arg != 'op':
            raise ValueError("Invalid keyword argument.")
        elif type(op) is not str:
            raise TypeError("Value for keyword argument 'op' must be a string.")
        elif op not in ['+', '*', 'max']:
            raise ValueError("Invalid keyword argument.")
        else:
            if op == '+':
                return sum(intList)
            elif op == '*':
                prod = 1
                if len(intList) == 0:
                    return prod
                for num in intList:
                    prod *= num
                return prod
            c = intList.copy()
            c.append(0)
            return max(c)

# Part B: Pitfalls: Exception handling
# Ex B.1
# import sys
#
# def sum_of_key_values(dict, key1, key2):
#     '''Return the sum of the values in the dictionary stored at key1 and key2.'''
#     try:
#         return dict[key1] + dict[key2]
#     except KeyError:
#         quit()

# When doing exception handling, you want to provide detailed explanations
# telling why the exception was reached. In this example, the function simply
# quits when the error is received. Instead, you'd want to do something like:
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        print("Invalid key value.", file=sys.stderr)

# Ex B.2
# import sys
#
# def sum_of_key_values(dict, key1, key2):
#     '''Return the sum of the values in the dictionary stored at key1 and key2.'''
#     try:
#         return dict[key1] + dict[key2]
#     except KeyError:   # raised if a key isn't in a dictionary
#         print('key not found!', file=sys.stderr)
# I'm actually not sure what's wrong with this code.

# Ex B.3
# def sum_of_key_values(dict, key1, key2):
#     '''Return the sum of the values in the dictionary stored at key1 and key2.'''
#     try:
#         return dict[key1] + dict[key2]
#     except KeyError:   # raised if a key isn't in a dictionary
#         raise KeyError

# Doesn't give a meaningful error message when a KeyError comes up. Instead,
# should write something like:
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError: # raised if a key isn't in a dictionary
        print("Invalid key value.", file=sys.stderr)

# Ex B.4
# def sum_of_key_values(dict, key1, key2):
#     '''Return the sum of the values in the dictionary stored at key1 and key2.'''
#     try:
#         val1 = dict[key1]
#     except KeyError as e:
#         raise e
#
#     try:
#         val2 = dict[key2]
#     except KeyError as e:
#         raise e
#
#     return val1 + val2

# Like the previous problem, the code is redundant in that the same error is
# raised after it was already caught by the try except block. Additionally, it
# does not tell which key is giving the error (which one doesn't actually exist
# in the dictionary).
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        val1 = dict[key1]
    except KeyError as e:
        print("Invalid key! key1 was not found in dict.", file=sys.stderr)

    try:
        val2 = dict[key2]
    except KeyError as e:
        print("Invalid key! key2 was not found in dict.", file=sys.stderr)

    return val1 + val2

# Ex B.5
# import sys
#
# def fib(n):
#     '''Return the nth fibonacci number.'''
#     if n < 0:
#         raise ValueError
#         print('n must be >= 0', file=sys.stderr)
#     elif n < 2:
#         return n  # base cases: fib(0) = 0, fib(1) = 1.
#     else:
#         return fib(n-1) + fib(n-2)

# The problem with the code here is when the exception is raised. The print
# statement after the exception is raised is never actually run because the
# exception is raised first. Instead, write:
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex B.6
# import sys
#
# def fib(n):
#     '''Return the nth fibonacci number.'''
#     if n < 0:
#         print('n must be >= 0', file=sys.stderr)
#         raise ValueError
#     elif n < 2:
#         return n  # base cases: fib(0) = 0, fib(1) = 1.
#     else:
#         return fib(n-1) + fib(n-2)

# Similarly to the previous problem, the print statement should be put into the
# exception instead of keeping it separate:
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex B.7
# from math import exp
#
# def exp_x_over_x(x):
#     '''
#     Return the value of e**x / x, for x > 0.0 and
#     e = 2.71828... (base of natural logarithms).
#     '''
#     if x <= 0.0:
#         raise TypeError('x must be > 0.0')
#     return (exp(x) / x)

# The function here is raising the wrong type of error in this case. x <= 0.0
# is not a conflict of types. Instead, a ValueError should be raised.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

# Ex B.8
from math import exp

# def exp_x_over_x(x):
#     '''
#     Return the value of e**x / x, for x > 0.0 and
#     e = 2.71828... (base of natural logarithms).
#     '''
#     if type(x) is not float:
#         raise Exception('x must be a float')
#     elif x <= 0.0:
#         raise Exception('x must be > 0.0')
#     return (exp(x) / x)

# The problem here is that the exception is not specific to the actually error
# that occurs. When x is not a float, a TypeError should be raised. When it is
# less than 0.0, a ValueError should be raised.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
