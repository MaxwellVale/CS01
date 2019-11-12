# Name:
# CMS cluster login:

import random, sys, time

# Pitfalls section omitted.

# ---------------------------------------------------------------------- 
# Part 2: Simple functions.
# ---------------------------------------------------------------------- 

import random, sys

#
# Problem 2.1
#

def draw_checkerboard(n):
    '''
    Return a string that, when printed, will draw an (nrows x ncols) 
    checkerboard on the terminal, where 'nrows' and 'ncols' are positive 
    integers.  

    The light squares are blank, the dark squares have a '#' character.
    The board is made up of lines and corners.
    Corners are represented by '+' characters.
    Horizontal lines are represented by '-' characters.
    Vertical lines are represented by '|' characters.
    The lower-left square of the bottommost row is blank.

    Arguments:
      nrows: the number of rows
      ncols: the number of columns

    Return value: a string representing the checkerboard, suitable for printing
      to the terminal.  The string, when printed, will have a blank line before
      and after the checkerboard.
      
    '''

    assert nrows >= 1
    assert ncols >= 1

    pass  # TODO

def test_draw_checkerboard():
    print(draw_checkerboard(1, 1))
    print(draw_checkerboard(1, 2))
    print(draw_checkerboard(2, 1))
    print(draw_checkerboard(2, 2))

    print(draw_checkerboard(4, 4))
    print(draw_checkerboard(4, 5))
    print(draw_checkerboard(5, 4))
    print(draw_checkerboard(5, 5))

    print(draw_checkerboard(8, 8))

#
# Problem 2.2
#

def roll_count(lst):
    '''
    Return a dictionary containing the count of all numbers
    in the list.

    Argument: a list of length 5, of ints in the range [1-6]
    '''

    pass  # TODO

def yahtzee_classify(lst):
    '''
    For a list of 5 numbers in the range 1-6, figure out which Yahtzee category
    they belong to.  The categories are:

      Yahtzee:         5 of one number
      Four of a kind:  4 of one number 
      Full house:      3 of one number and 2 of another
      Large straight:  5 consecutive numbers
      Small straight:  4 consecutive numbers
      Three of a kind: 3 of one number
      Chance:          anything else

    The categories are mutually exclusive.  For instance, a Yahtzee is not
    also considered four of a kind or three of a kind, and a full house is
    not a three of a kind.  Always choose the highest possible rank for the
    hand.  Ranks are ordered (from high to low):

      Yahtzee > Four of a kind > Full house 
        > Large straight > Small straight 
        > Three of a kind > Chance

    Return the category as a string; one of:
      'YAHTZEE', 'FOUR OF A KIND', 'FULL HOUSE',
      'LARGE STRAIGHT', 'SMALL STRAIGHT', 
      'THREE OF A KIND', 'CHANCE'
    '''

    pass  # TODO


# Supplied to students.
def yahtzee_roll():
    '''
    Make a random roll of five dice and return a list of the results.
    '''

    lst = []
    for i in range(5):
        roll = random.randint(1, 6)
        lst.append(roll)
    lst.sort()
    return lst

#
# Problem 2.3
#


import random

def nim_done(lst):
    '''
    Return True if the list 'lst' contains all zeros.
    '''

    pass  # TODO

def nim_sum(lst):
    '''
    Compute and return the Nim sum of a list of non-negative integers.
    The Nim sum is the exclusive or of all the items in the list.
    '''

    pass  # TODO

def nim_random_move(lst):
    '''
    Make a random move in a Nim game.
    
    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the random move, # to remove)
    '''

    pass  # TODO

def nim_best_move(lst):
    '''
    Compute the optimal nim move in a list of non-negative integers.
    Return the index of the list and how many to remove from that location.

    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the best move, # to remove)
    '''

    pass  # TODO

#
# Supplied to students:
#

def nim_show(lst):
    '''
    Display a nim board.
    '''

    print('Nim: ', end='')
    for item in lst:
        print(item, end=' ')
    print('\n')  # two newlines

def nim_get_move(lst):
    '''
    Get a move from the player in a Nim game.  Do error checking.
    Repeat until a valid move is entered.
    '''

    try_again = 'Invalid move -- try again.\n'

    while True:
        move = input('Enter your move (index, n): ')
        move = move.split()

        # Error checking.
        if len(move) != 2:
            print('Error: input must be two numbers.')
            print(try_again)
            continue

        (i, n) = move

        try:
            i = int(i)
            n = int(n)
        except ValueError:
            print('Error: index and n must both be ints')
            print(try_again)
            continue

        if i < 0 or i > len(lst):
            print('Error: index out of range')
            print(try_again)
            continue

        if n <= 0:
            print('Error: number to be removed is too small')
            print(try_again)
            continue

        if lst[i] < n:
            print('Error: number to be removed is too large')
            print(try_again)
            continue

        return (i, n)


def nim_play(lst):
    '''
    Play a game of nim against the computer, given a starting list.
    '''

    while True:
        nim_show(lst)

        # Computer moves.
        (i, n) = nim_best_move(lst)
        print(f'Computer moves: {i} {n}\n')

        lst[i] -= n
        if nim_done(lst):
            print('Computer wins!')
            break

        nim_show(lst)

        # Human player moves.
        (i, n) = nim_get_move(lst)

        lst[i] -= n
        if nim_done(lst):
            print('You win!')
            break

# ---------------------------------------------------------------------- 
# Miniproject: The 3's game.
# ---------------------------------------------------------------------- 

def make_board():
    '''
    Create a game board in its initial state.

    The board is a dictionary mapping (row, column) coordinates (zero-indexed)
    to integers which are all initially either 1, 2, or 3.  There are 4 rows and
    4 columns.  Empty locations are not stored in the dictionary.  Exactly 9
    randomly-chosen locations are initially filled. At least one each of 1, 2, 3
    must be present; the other six locations are filled at random with a 1, 2 or
    3.

    Arguments: none
    Return value: the board
    '''

    pass  # TODO

#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''

    assert 0 <= row_n < 4
    pass  # TODO

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4
    pass  # TODO

def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= row_n < 4
    assert len(row) == 4
    pass  # TODO

def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= col_n < 4
    assert len(col) == 4
    pass  # TODO

#
# Problem 3.3
#

def can_merge(n1, n2):
    '''
    Return True if two numbers can be merged according to the
    rules of the Threes game.
    '''

    pass  # TODO


def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    Threes game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.

    Note: the original list is not altered.
    '''

    assert len(numbers) == 4
    pass  # TODO

#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']
    pass  # TODO

#
# Problem 3.5
#

def game_over(board):
    '''
    Return True if the game is over i.e. if no moves can be made on the board.
    The board is not altered.

    Argument: board -- the game board
    Return value: True if the game is over, else False
    '''

    pass  # TODO



#
# Problem 3.6
#

def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board has changed,
    then add a new number (1, 2 or 3, equal probability) on an empty edge square
    on the opposite side of the board to the move. (So if the move was to the
    left, add a number to an empty square on the right edge of the board.) If
    there is more than one empty edge square that can be filled, choose one at
    random.

    This function assumes that a move can be made on the board.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    pass  # TODO


#
# Supplied to students:
#

def opposite_edge(cmd):
    '''
    Given a movement command, return the locations of squares which are
    eligible to be filled with a new number.

    Argument: cmd: one letter ('w', 's', 'a', or 'd')
    Return value: a list of (row, column) locations
    '''

    if cmd == 'w':    # up
        return [(3, 0), (3, 1), (3, 2), (3, 3)]  # bottom edge
    elif cmd == 's':  # down
        return [(0, 0), (0, 1), (0, 2), (0, 3)]  # top edge
    elif cmd == 'a':  # left
        return [(0, 3), (1, 3), (2, 3), (3, 3)]  # right edge
    elif cmd == 'd':  # right
        return [(0, 0), (1, 0), (2, 0), (3, 0)]  # left edge

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        if game_over(b):
            print('Game over!')
            break

        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        display(b)


#
# Useful for testing:
#

def list_to_board(lst):
    '''
    Convert a length-16 list into a board.
    '''
    board = {}
    k = 0
    for i in range(4):
        for j in range(4):
            if lst[k] != 0:
                board[(i, j)] = lst[k]
            k += 1
    return board 

def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        display(board)
        if game_over(board):
            break

