# Name: Maxwell Vale
# CMS cluster login: mvale

import random, sys, time

# ----------------------------------------------------------------------
# Part 1: Pitfalls
# ----------------------------------------------------------------------

# Problem 1.1
# def fiblist('n'):
#    'Return a list of all fibonacci numbers (starting from 0, 1) which are
#    less than n.  Assume n is a non-negative integer.'
#     if n = 0:
#         return []
#     elif n <= 1:
#         return [0]
#     else:
#         fibs = [0, 1]
#         while True
#             fib_next = fibs[-1] + fibs[-2]
#             if fib_next >= n:
#                 return fibs
#             fibs.append(fib_next)
#
# Syntax Errors:
# 1. def fiblist('n') --> The arguments for the function should be written as
# variables, meaning it should not be surrounded by quotes. Having the argument
# in quotes means that the references to a variable n won't work.
# 2. Docstring --> The docstring runs over multiple lines, yet it only uses
# single quotes to do so. Instead triple quotes should be used to have a string
# span over multiple lines.
# 3. if n = 0: --> The if statement is supposed to check the truth value of
# some boolean statement passed to it. n = 0 is assigning the variable n to have
# the value of 0 instead of checking its equality with 0. The code should read
# if n == 0: instead.
# 4. while True --> There is no colon following the end of this while loop. \
# 5. Indentation --> The indent of the docstring and the subsequent code is not
# aligned. The docstring and the following if statement are not lined up.

# Problem 1.2
# def obfuscate(line):
#     '''
#     Obfuscate a line by changing some punctuation to spaces,
#     permuting the vowels, and replacing some characters with #s.
#     '''
#
#     substitutions = {
#       'a' : 'e',
#       'e' : 'i',
#       'i' : 'o',
#       'o' : 'u',
#       'u' : 'a',
#       ['v', 'x', 'z', 'j', 'q'] : '#',
#       [',', '.', '?', '!'] : ' '
#     }
#
#     for i in enumerate(line):
#         char = line[i]
#         done = False
#         for (key, sub) in substitutions:
#             if char in key:
#                 line[i] = sub
#                 done == True
#         if not done:
#             line[i] = char
#
# Semantic Errors:
# 1. char = line[i] --> Trying to set char to one of the letters in string line.
# However, i is not an integer, so you cannot index line by i.
# 2. Keys in dictionary need to be immutable. However, substitutions has lists
# as some its keys, so they are invalid.
# 3. for (key, sub) in substitutions: --> Trying to retrieve the key value pairs
# from substitutions, but can't do it this way. May use the items() function in
# order to access both the keys and the values of substitutions.
# 4. line[i] = sub --> Strings are immutable. Since line is a string, you cannot
# change the string at individual indices after it has already been created.
# 5. done == True --> The equality of done and True is checked here instead of
# setting done to True.
# 6. ehh

# Problem 1.3
# def rip(n):
#  '''Resv ls ip'''
#  l=len(n)
#  if l<2: return #bc
#  x=0
#  l2=l//2
#  while True:
#         if x >=l2:
#            break
#         else:
#            pass
#         o= l-x-1
#         (n[x],n[o])=(n[o],n[x])
#         x+=1
#
# Style Errors:
# 1. [INDENT_CONSISTENT]
# 2. [BAD_NAMES]
# 3. [STMTS_ON_LINE]
# 4. [COMMENT_GRAMMATICAL]
# 5. [OPERATOR_SPACE]
# 6. [COMMA_SPACE]

# ----------------------------------------------------------------------
# Part 2: Simple functions.
# ----------------------------------------------------------------------

import random, sys

#
# Problem 2.1
#

def draw_checkerboard(nrows, ncols):
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

    checkerStr = '\n'
    for row in range(nrows):
        checkerStr += '+-' * ncols + '+\n'
        line = ''
        for col in range(ncols):
            if (row + col + nrows) % 2 != 0:
                line += '|#'
            else:
                line += '| '
        checkerStr += line + '|\n'
    return checkerStr + '+-' * ncols + '+\n'

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
    countDict = {}
    for n in range(1, 7):
        if n in lst:
            countDict[n] = lst.count(n)
    return countDict

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

    countRolls = roll_count(lst)
    if max(countRolls.values()) == 5:
        return 'YAHTZEE'
    elif max(countRolls.values()) == 4:
        return 'FOUR OF A KIND'
    elif max(countRolls.values()) == 3:
        if len(countRolls.values()) > 2:
            return 'THREE OF A KIND'
        else:
            return 'FULL HOUSE'
    else:
        large = [set([1, 2, 3, 4, 5]), set([2, 3, 4, 5, 6])]
        small = [set([1, 2, 3, 4]), set([2, 3, 4, 5]),\
                 set([3, 4, 5, 6])]
        nonDups = set(countRolls.keys())
        if nonDups in large:
            return 'LARGE STRAIGHT'
        elif nonDups in small or len(nonDups) == 5:
            return 'SMALL STRAIGHT'
        else:
            return 'CHANCE'

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

# for i in range(12):
#     x = yahtzee_roll()
#     print(x)
#     print(yahtzee_classify(x))


#
# Problem 2.3
#


import random

def nim_done(lst):
    '''
    Return True if the list 'lst' contains all zeros.
    '''
    return lst == [] or (len(set(lst)) == 1 and 0 in set(lst))


def nim_sum(lst):
    '''
    Compute and return the Nim sum of a list of non-negative integers.
    The Nim sum is the exclusive or of all the items in the list.
    '''
    if len(lst) == 0:
        return 0
    else:
        return lst[0] ^ nim_sum(lst[1:])

def nim_random_move(lst):
    '''
    Make a random move in a Nim game.

    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the random move, # to remove)
    '''
    indices = []
    for i in range(len(lst)):
        if lst[i] > 0:
            indices.append(i)
    index = random.choice(indices)
    return (index, random.randint(1, lst[index]))

def nim_best_move(lst):
    '''
    Compute the optimal nim move in a list of non-negative integers.
    Return the index of the list and how many to remove from that location.

    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the best move, # to remove)
    '''
    nSum = nim_sum(lst)
    diffList = [x - (x ^ nSum) for x in lst]
    for n in diffList:
        if n > 0:
            return (diffList.index(n), n)
    return nim_random_move(lst)

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
    board = {}
    while len(board) < 9:
        pos = (random.randint(0,3), random.randint(0,3))
        if pos not in board:
            if len(board) < 3:
                board[pos] = len(board) + 1
            else:
                board[pos] = random.choice([1, 2, 3])
    return board

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
    r = [0, 0, 0, 0]
    for row, col in board:
        if row == row_n:
            r[col] = board[(row, col)]
    return r

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4
    c = [0, 0, 0, 0]
    for row, col in board:
        if col == col_n:
            c[row] = board[(row, col)]
    return c

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
    for i in range(4):
        if row[i] != 0:
            board[(row_n, i)] = row[i]
        elif (row_n, i) in board:
            del board[(row_n, i)]

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
    for i in range(4):
        if col[i] != 0:
            board[(i, col_n)] = col[i]
        elif (i, col_n) in board:
            del board[(i, col_n)]

#
# Problem 3.3
#

def can_merge(n1, n2):
    '''
    Return True if two numbers can be merged according to the
    rules of the Threes game.
    '''

    return (set([n1, n2]) == set([1, 2])) or (n1 > 2 and n2 > 2 and n1 == n2)


def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    Threes game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.

    Note: the original list is not altered.
    '''

    assert len(numbers) == 4
    nums = numbers.copy()
    haveMerged = False
    for i in range(3):
        index = i + 1
        if can_merge(nums[index - 1], nums[index]):
            if not haveMerged:
                nums[index - 1] = nums[index - 1] + nums[index]
                nums[index] = 0
                haveMerged = True
        elif nums[index - 1] == 0:
            nums[index - 1] = nums[index]
            nums[index] = 0
    return nums



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
    for i in range(4):
        if cmd == 'w' or cmd == 's':
            lst = get_column(board, i)
        else:
            lst = get_row(board, i)
        if cmd == 's' or cmd == 'd':
            lst.reverse()
            lst = make_move_on_list(lst)
            lst.reverse()
        else:
            lst = make_move_on_list(lst)
        if cmd == 'w' or cmd == 's':
            put_column(board, lst, i)
        else:
            put_row(board, lst, i)


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

    b = board.copy()
    cmds = ['w', 'a', 's', 'd']
    for cmd in cmds:
        make_move(b, cmd)
        if b != board:
            return False
    return True


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

    b = board.copy()
    make_move(board, cmd)
    if board != b:
        positions = opposite_edge(cmd)
        emptyPos = []
        for pos in positions:
            if pos not in board:
                emptyPos.append(pos)
        board[random.choice(emptyPos)] = random.choice([1,2,3])


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
