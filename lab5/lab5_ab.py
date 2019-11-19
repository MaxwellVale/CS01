# Maxwell Vale
# CS01 Section 1a
# Assignment 5

import math

# Part A: Exercises
# Ex A.1
class Point():
    '''
    Class Point
    A class representing a point in three-dimensional Euclidean space (x, y, z).

    Methods
    distanceTo
    '''

    def __init__(self, x, y, z):
        '''
        Initializing a Point with its x, y, and z coordinates.
        '''
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, point):
        '''
        Function distanceTo
        Computes the distance between the current Point and a second point.

        Arguments
        point --> Another Point object.

        Return
        Returns the distance between the current Point and the argument point.
        '''
        return math.sqrt((self.x - point.x) ** 2 +
                         (self.y - point.y) ** 2 +
                         (self.z - point.z) ** 2)

# Ex A.2
class Triangle():
    '''
    Class Triangle
    A class representing a triangle in the three-dimensional Euclidean space.

    Methods
    area
    '''

    def __init__(self, p1, p2, p3):
        '''
        Creates a new Triangle using its three vertices.
        '''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        '''
        Function area
        Returns the area of the Triangle defined by points p1, p2, and p3.
        Utilizes Heron's formula to calculate the area.

        Arguments
        No arguments.

        Return
        Returns the area of the Triangle.
        '''
        a = self.p1.distanceTo(self.p2)
        b = self.p1.distanceTo(self.p3)
        c = self.p2.distanceTo(self.p3)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Ex A.3
class Averager():
    '''
    Class Averager
    A class that stores a list of numbers and performs various operations on the
    list.

    Methods
    getNums
    append
    extend
    average
    limits
    '''

    def __init__(self):
        '''
        Initializes the variables of Averager instance.
        No initialization arguments.
        '''
        self.nums = []
        self.total = 0
        self.n = 0

    def getNums(self):
        '''
        Returns a copy of the list of numbers, nums.
        '''
        return self.nums[:]

    def append(self, num):
        '''
        Adds a new number, num, to the list of numbers, nums.
        '''
        self.nums.append(num)
        self.total += num
        self.n += 1

    def extend(self, lst):
        '''
        Appends a list of numbers, lst, to the end of the list of numbers, nums.
        '''
        self.nums += lst
        self.total += sum(lst)
        self.n += len(lst)

    def average(self):
        '''
        Returns the average of the list of numbers, nums, as a floating point
        number. When there are no elements in the list, returns 0.0.
        '''
        if self.n == 0:
            return 0.0
        return float(self.total / self.n)

    def limits(self):
        '''
        Returns the minimum and maximum values of the list of numbers, nums,
        in a tuple. If there are no elements in nums, then returns (0, 0).
        '''
        if self.n == 0:
            return (0, 0)
        return (min(self.nums), max(self.nums))

# Part B: Pitfalls: Poor design
# Ex B.1
# def is_positive(x):
#     '''Test if x is positive.'''
#     if x > 0:
#         return True
#     else:
#         return False
# There is more code than needed here. Since we are checking if x is positive or
# not and x > 0 already returns True or False, then we may just return x > 0.
# The code should actually be
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# Ex B.2
# def find(x, lst):
#     '''Returns the index into a list where x is found, or -1 otherwise.
#     Assume that x is found at most once in the list.'''
#     found = False
#     location = -1
#     for i, item in enumerate(lst):
#         if item == x:
#             found = True
#             location = i
#     if found == True:
#         return location
#     else:
#         return -1
# This method of finding the index is unnecessarily complex. You don't need to
# have the boolean found to find out what to return. If the item is never found,
# location still has -1 as its value, so simply returning location at the end
# works too. Instead, the code should be:
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    location = -1
    for i, item in enumerate(lst):
        if item == x:
            location = i
            break
    return location

# Ex B.3
# def categorize(x):
#     '''Return a string categorizing the number 'x', which should be
#     an integer.'''
#     if x < 0:
#         category = 'negative'
#     if x == 0:
#         category = 'zero'
#     if x > 0 and x < 10:
#         category = 'small'
#     if x >= 10:
#         category = 'large'
#     return category
# This code is both excessive and inefficient. First, the code has to run through
# every if statement even though only one can be true at once (they are all
# mutually exclusive events). Instead, the elif statement should be used.
# Additionally, since the catergories are mutually exclusive, you don't need to
# wait until the end of the function to return the category. Instead, a return
# statement can be put inside each if statement:
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x < 10:
        return 'small'
    return 'large'

# Ex B.4
# def sum_list(lst):
#     '''Returns the sum of the elements of a list of numbers.'''
#
#     if len(lst) == 0:
#         answer = 0
#     elif len(lst) == 1:
#         answer = lst[0]
#     elif len(lst) == 2:
#         answer = lst[0] + lst[1]
#     elif len(lst) > 2:
#         total = 0
#         for item in lst:
#             total += item
#         answer = total
#     return answer
# This code is very inefficient. Instead of covering the cases of length 0, 1,
# and 2 separately, they can be taken care of with one simple algorithm.
# The last elif looks similar to what the actual code should be like. There
# is also excessive code in that the varbiable answer is given the value of the
# variable total and then returned. Instead, you can just return total:
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''

    total = 0
    for item in lst:
        total += item
    return total
