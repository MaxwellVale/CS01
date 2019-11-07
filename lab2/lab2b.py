# Maxwell Vale
# CS01 Section 1a
# Assignment 2

import random

# Ex D.1
def make_random_code():
    '''
    Function make_random_code
    Makes a random four letter code from the elements of [colors]

    Arguments
    Takes no arguments

    Return
    Returns a four letter code as a string
    '''
    colors = ['R', 'G', 'B', 'Y', 'O', 'W']
    code = ''
    for i in range(4):
        code += random.choice(colors)
    return code
# print(make_random_code())

# Ex D.2
def count_exact_matches(str1, str2):
    '''
    Function count_exact_matches
    Counts how many corresponding elements(same element in same position)
    the two strings have

    Arguments
    str1, str2 --> Strings with length 4 composed of r, g, b, y, o, and w

    Return
    Returns an integer representing the number of exact matches between str1 and str2
    '''
    matches = 0
    for index in range(4):
        if str1[index] == str2[index]:
            matches += 1
    return matches


# print(count_exact_matches('RGBY', 'RGBY'))  # --> 4
# print(count_exact_matches('RGBY', 'GBYR'))  # --> 0
# print(count_exact_matches('RGBY', 'RGOO'))  # --> 2
# print(count_exact_matches('RGBY', 'RWBW'))  # --> 2
# print(count_exact_matches('RGBY', 'WOWO'))  # --> 0

# Ex D.3
def count_letter_matches(str1, str2):
    '''
    Function count_letter_matches
    Counts the number of letter matches without necessarily matching in position

    Arguments
    str1, str2 --> Strings with length 4 composed of r, g, b, y, o, and w

    Return
    Returns an integer representing the number of letter matches between str1 and str2
    '''
    strList = list(str2)
    matches = 0
    for index in range(4):
        if str1[index] in strList:
            strList.remove(str1[index])
            matches += 1
    return matches

# print(count_letter_matches('RGBY', 'RGBY'))  # --> 4
# print(count_letter_matches('RGBY', 'WOWO'))  # --> 0
# print(count_letter_matches('RGBY', 'GBYR'))  # --> 4
# print(count_letter_matches('ROGO', 'RRGG'))  # --> 2
# print(count_letter_matches('RGBY', 'OROG'))  # --> 2
# print(count_letter_matches('RGBY', 'BWBR'))  # --> 2
# print(count_letter_matches('RBBY', 'GRBO'))  # --> 2

# Ex D.4
def compare_codes(code, guess):
    '''
    Function compare_codes
    Compares the secret code and the guess code for similarities and outputs the
    key peg string representing the matches between the two codes

    Arguments
    code --> secret code generated by make_random_code()
    guess --> guessed code sequence

    Return
    Returns the key peg string that represents the number of exact matches and
    letter matches
    '''
    blackPegs = count_exact_matches(code, guess)
    whitePegs = count_letter_matches(code, guess) - blackPegs
    blankPegs = 4 - (blackPegs + whitePegs)
    return blackPegs * 'b' + whitePegs * 'w' + blankPegs * '-'

# print(compare_codes('RGBY', 'RGBY'))  # --> 'bbbb'
# print(compare_codes('RGBY', 'WOWO'))  # --> '----'
# print(compare_codes('RGBY', 'YBGR'))  # --> 'wwww'
# print(compare_codes('ROBO', 'RWBW'))  # --> 'bb--'
# print(compare_codes('RBGY', 'RGBY'))  # --> 'bbww'

def run_game():
    '''
    Function run_game
    Runs the Mastermind game. Creates a random code and prompts the user to
    guess the code until the code is successfully guessed. Tells the user how
    close the guess is to the code by comparing the two. Tracks the number of
    guesses required to geuss the code.

    Arguments
    No arguments

    Returns
    No return value
    '''
    print("New game.")
    secretCode = make_random_code()
    # First guess
    moves = 0
    comparison = ''
    while comparison != 'bbbb':
        guess = input("Enter your guess: ")
        guess = guess.upper()
        comparison = compare_codes(secretCode, guess)
        print("Result: " + comparison)
        moves += 1
    print("Congratulations! You cracked the code in " + str(moves) + " moves!")

#run_game()