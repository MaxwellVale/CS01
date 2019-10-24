# Maxwell Vale
# CS01 Section 1a
# Assignment 2

import random

# Part B: Exercises
# Ex B.1
def complement(sequence):
    '''
    Function complement
    Takes a string representing a DNA sequence and returns the DNA complement
    of the DNA sequence. It does this by replacing 'A's with 'T's, 'T's with 'A's,
    'C's with 'G's. and 'G's with 'C's.

    Arguments
    sequence --> A string comprised of only 'A's, 'T's, 'C's, and 'G's (DNA String)

    Return
    Returns the complement string to the DNA string in the argument
    '''
    compSeq = ''
    seq = sequence.upper()
    for i in seq:
        if i == 'A':
            compSeq += 'T'
        elif i == 'T':
            compSeq += 'A'
        elif i == 'C':
            compSeq += 'G'
        else:
            compSeq += 'C'
    return compSeq

# Ex B.2
def list_complement(sequenceList):
    '''
    Function list_complement
    Takes a list representing a DNA sequence and returns the DNA complement
    of the DNA sequence as a list. It does this by replacing 'A's with 'T's,
    'T's with 'A's, 'C's with 'G's. and 'G's with 'C's.

    Arguments
    sequence --> A list in which each element is a single 'A', 'T', 'C', or 'G'

    Return
    Returns the complement DNA sequence as a list
    '''
    for index in range(len(sequenceList)):
        if sequenceList[index] == 'A':
            sequenceList[index] = 'T'
        elif sequenceList[index] == 'T':
            sequenceList[index] = 'A'
        elif sequenceList[index] == 'G':
            sequenceList[index] = 'C'
        else:
            sequenceList[index] = 'G'

# Ex B.3
def product(numList):
    '''
    Function prodcut
    Computes and returns the product of the elements of a number list

    Arguments
    numList --> A list composed of numbers

    Return
    Returns the product of all the numbers in numList
    '''
    if len(numList) == 0:
        return 1
    else:
        product = numList[0]
        for num in numList[1:]:
            product *= num
        return product

# Ex B.4
def factorial(n):
    '''
    Function factorial
    Computes and returns n!

    Arguments
    n --> Some integer >= 0

    Return
    Returns the value of n! as an integer
    '''
    return product(range(n+1)[1:])

# Ex B.5
def dice(m, n):
    '''
    Function dice
    Simulates the rolling of a certain number, n, amount of m sided dice.
    It sums up the results of all n dice.

    Arguments
    m --> Number of sides on the dice
    n --> Number of dice rolled

    Return
    Returns an integer representing the sum of all the rolls
    '''
    sumRolls = 0
    for roll in range(n):
        sumRolls += random.choice(range(m+1)[1:])
    return sumRolls

# Ex B.6
def remove_all(lst, element):
    '''
    Function remove_all
    Removes all occurrences of element from lst by counting how many times
    element occurs in lst and removing every time the occurrences > 0

    Arguments
    lst --> A list of integers
    element --> The element to be removed from lst

    Return
    Does not return anything. Alters lst.
    '''
    while(lst.count(element)) > 0:
        lst.remove(element)

# Ex B.7
def remove_all2(lst, element):
    '''
    Function remove_all
    Removes all occurrences of element from lst by counting the number of
    occurrences of element in lst and removing from lst that number of times

    Arguments
    lst --> A list of integers
    element --> The element to be removed from lst

    Return
    Does not return anything. Alters lst.
    '''
    occurrences = lst.count(element)
    for i in range(occurrences):
        lst.remove(element)

def remove_all3(lst, element):
    '''
    Function remove_all
    Removes all occurrences of element from lst by removing element from lst
    as long as an element exists in lst

    Arguments
    lst --> A list of integers
    element --> The element to be removed from lst

    Return
    Does not return anything. Alters lst.
    '''
    while element in lst:
        lst.remove(element)

# Ex B.8
def any_in(l1, l2):
    '''
    Function any_in
    Tells you if any of the elements of l1 are in l2

    Arguments
    l1, l2 --> Both are lists

    Return
    True --> If any of the elements of l1 appear in l2
    False --> If none of the elements of l1 appear in l2
    '''
    for element in l1:
        if element in l2:
            return True
    return False

# Part C: Pitfalls
# Ex C.1.a
# There is a fault in the code at the if statement. The if requires a boolean
# value in order to operate, but it is given a = 0 instead, so the code will
# not work. a = 0 is assigning a to have the value 0 rather than check if a
# is equal to 0. Instead the code should have a == 0, which will return true
# or false depending on whether the value of a is actually 0.
# if a == 0:
#   print('a is zero!')

# Ex C.1.b
# There should not be quotes around the s in the argument list. This makes
# the reference to s later in the function invalid because it does not exist
# within the function and the variables in the argument list are not allowed to
# have quotes around them. You can fix it by removing the quotation marks.
# def add_suffix(s):

# Ex C.1.c
# Here, the function will always return the string 's-Caltech' because the
# return statement is written as return 's' + '-Caltech'. This simply
# concatenates the strings 's' and '-Caltech' together rather than adding
# '-Caltech' to the end of the string represented by variable s.
# return s + '-Caltech'

# Ex C.1.d
# The last statement lst = lst + bam is not correct because you cannot add
# an iterable (list) and an integer together. Instead you want to APPEND the
# string 'bam' to the end of the list of strings. So, you would want to write
# lst.append('bam')

# Ex C.1.e
# This code is incorrect because it is using the return values of several
# list functions. Firstly, it is setting lst2 to be the return value of
# lst.reverse(). This is incorrect because the lst.reverse() function returns
# None, meaning that lst2 now has the value of None, but lst is still reversed.
# Instead, remove the new variable and just alter lst.
# lst.reverse()
# lst.append(0)
# return lst (if you want)

# Ex C.1.f
# The fault in the code is at the last line list.append(letters). The
# list.append(item) function takes the item and adds it as the last element
# in list. Thus, list.append(letters) will result in list having the entirety
# of letters as its last element, as opposed to combining the two lists.
# list += letters

# Ex C.2
# When variable c is defined, the right side of the assignment reads b + a.
# When the values are substituted in, it becomes c = 20 + 10 --> c = 30. The
# assignment of c to b + a means to give it whatever the value of b + a was at
# the time of assignment. It doesn't mean that c will always equal b + a as the
# values of b and a change.

# Ex C.3
# The first function would work because the statement n = 2 * add_and_double_1(1,2,3)
# means 2 * (RETURN VALUE of add_and_double_1(1,2,3)). Since add_and_double_1()
# actually returns an integer, then the statement will work. However,
# add_and_double_2(1,2,3) does not have a return statement (it merely prints
# the result). Thus, n = 2 * add_and_double_2(1,2,3) will become
# n = 2 * None, because the second function does not RETURN an integer.

# Ex C.4
# The second example would not work because the sum_of_squares_2() function is
# not defined with any arguments in its parameters list. Thus, writing
# sum_of_squares_2(2,3) would not work because the function itself does not
# take any arguments. This is opposed to sum_of_squares_1 which actually does
# have arguments in its parameter list. The function itself still works because
# it retrieves a value for x and y through user INPUT.

# Ex C.5
# This function tries to modify the elements in the string s. However, in python
# strings are immutable, so you are not allowed to alter the individual characters
# in the string. So, saying s[0] = 'anyString' would not work because you cannot
# assign an item to s[0]. Instead, you might want to do
# s = s[0].upper() + s[1:]

# Ex C.6
# This function won't work because it is not actually altering the value of each
# element in the list. When using the for loop through the elements, the variable
# item is given the same value as the corresponding element in the list. Thus,
# writing item *= 2 will alter the value of item, but not the value in the
# actual list. item is simply referencing an element of list.
