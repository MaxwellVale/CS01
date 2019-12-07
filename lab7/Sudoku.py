# Maxwell Vale
# CS01 Section 1a
# Assignment 7

'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuLoadError(SudokuError):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.moves = []
        self.board = []
        for i in range(9):
            self.board.append([0] * 9)


    def load(self, filename):
        with open(filename, 'r') as file:
            f = file.read()
            if f.count('\n') != 9:
                raise SudokuLoadError("Incorrect number of lines!")
            lines = f.split('\n')
            for i in range(9):
                if len(lines[i]) != 9:
                    raise SudokuLoadError("Lines must be 9 characters long!")
                try:
                    l = int(lines[i])
                    self.board[i] = [int(x) for x in list(lines[i])]
                except ValueError:
                    raise SudokuLoadError("Lines may only contain digits 0 to 9!")
            self.moves = []

    def save(self, filename):
        with open(filename, 'w') as file:
            for line in self.board:
                file.write(''.join([str(x) for x in line]))
                file.write('\n')

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print()
        print('  +-----+-----+-----+')
        print()

    def getRow(self, row):
        return self.board[row - 1]

    def getCol(self, col):
        column = []
        for row in self.board:
            column.append(row[col - 1])
        return column

    def getSquare(self, row, col):
        square = []
        sRow = (row - 1) // 3
        sCol = (col - 1) // 3
        for rowI in range(3):
            r = 3 * sRow + rowI
            for colI in range(3):
                c = 3 * sCol + colI
                square.append(self.board[r][c])
        return square

    def move(self, row, col, val):
        if (type(row) is not int or row < 1 or row > 9) or \
        type(col) is not int or col < 1 or col > 9:
            raise SudokuMoveError("Coordinates must be integers from 1 to 9.")
        elif type(val) is not int or val < 1 or val > 9:
            raise SudokuMoveError("Invalid value. Must be an integer from 0 to 9.")
        elif self.board[row - 1][col - 1] != 0:
            raise SudokuMoveError("Occupied space! Move needs to be made in an "
                                  + "empty position.")
        elif val in self.getRow(row):
            raise SudokuMoveError("Invalid move! Number already in this row.")
        elif val in self.getCol(col):
            raise SudokuMoveError("Invalid move! Number already in this column.")
        elif val in self.getSquare(row, col):
            raise SudokuMoveError("Invalid move! Number already in this square.")
        else:
            self.moves.append((row, col, val))
            self.board[row - 1][col - 1] = val

    def undo(self):
        last = self.moves.pop()
        self.board[last[0] - 1][last[1] - 1] = 0

    def solve(self):
        while True:
            try:
                cmd = input("What do you want to do? ")
                if len(cmd) == 3:
                    try:
                        move = [int(x) for x in list(cmd)]
                        self.move(move[0], move[1], move[2])
                        self.show()
                    except ValueError:
                        raise SudokuCommandError("Move should be a three digit "
                                                 + "sequence.")
                elif cmd == 'q':
                    print("Quitting... ")
                    return
                elif cmd == 'u':
                    print('Undoing the last move... ')
                    self.undo()
                    self.show()
                else:
                    cmd1 = cmd.split(' ')
                    print (cmd1)
                    if len(cmd1) != 2 or cmd1[0] != 's':
                        raise SudokuCommandError("Invalid command!")
                    print("Saving current state to " + cmd1[1])
                    self.save(cmd1[1])
            except SudokuCommandError as e:
                print(e)
            except SudokuMoveError as e:
                print(e)




if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except FileNotFoundError as e:
            print(e)
        except SudokuLoadError as e:
            print(e)

    s.show()
    s.solve()
