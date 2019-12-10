# Name: Maxwell Vale
# Login: mvale
'''
Rubik's cube class.
'''

import copy, random
import rubiks_utils as u
import rubiks_rep as r

class InvalidCube(Exception):
    '''
    This exception is raised when a cube has been determined to be in
    an invalid configuration.
    '''
    pass

class RubiksCube:
    '''
    This class implements all Rubik's cube operations.
    '''

    def __init__(self, size):
        '''Initialize the cube representation.'''
        # Cube representation.
        self.rep = r.RubiksRep(size)
        # Number of moves, quarter-turn metric.
        self.count = 0

    def get_state(self):
        '''
        Return a copy of the internal state of this object.
        '''
        rep = copy.deepcopy(self.rep)
        return (rep, self.count)

    def put_state(self, rep, count):
        '''
        Restore a previous state.
        '''
        self.rep = rep
        self.count = count

    ### Basic operations.

    def rotate_cube(self, axis, dir):
        '''
        Rotate the cube as a whole.
        The X axis means in the direction of an R turn.
        The Y axis means in the direction of a U turn.
        The Z axis means in the direction of an F turn.
        The + direction is clockwise.
        The - direction is counterclockwise.

        Arguments:
          axis -- one of ['X', 'Y', 'Z']
          dir  -- one of ['+', '-']

        Return value: none
        '''
        assert axis in ['X', 'Y', 'Z']
        assert dir in ['+', '-']
        turns = 1
        if dir == '-':
            turns += 2
        for i in range(turns):
            if axis == 'X':
                self.rep.rotate_cube_X()
            elif axis == 'Y':
                self.rep.rotate_cube_Y()
            else:
                self.rep.rotate_cube_Z()



    def move_face(self, face, dir):
        '''
        Move the specified face.
        Arguments:
          -- face: one of ['U', 'D', 'L', 'R', 'F', 'B']
          -- dir: '+' for clockwise or '-' for counterclockwise

        Return value: none
        '''
        assert face in ['U', 'D', 'F', 'B', 'L', 'R']
        assert dir in ['+', '-']
        turns = 1
        self.count += 1
        if dir == '-':
            turns += 2
        self.face_to_F(face)
        for i in range(turns):
            self.rep.move_F()
        self.F_to_face(face)


    def face_to_F(self, face):
        d = {'U' : ('X', '-'), 'D' : ('X', '+'), 'R' : ('Y', '+'), 'L' : ('Y', '-'), 'B' : ('Y', '+')}
        if face == 'F':
            return
        turn, dir = d[face]
        if face == 'B':
            self.rotate_cube(turn, dir)
        self.rotate_cube(turn, dir)

    def F_to_face(self, face):
        self.face_to_F(face)
        if face != 'B':
            for i in range(2):
                self.face_to_F(face)

    def random_rotations(self, n):
        '''
        Rotate the entire cube randomly 'n' times.

        Arguments:
          n -- number of random rotations to make

        Return value: none
        '''
        for _ in range(n):
            rot = random.choice('XYZ')
            dir = random.choice('+-')
            self.rotate_cube(rot, dir)

    def random_moves(self, n):
        '''
        Make 'n' random moves.

        Arguments:
          n -- number of random moves to make

        Return value: none
        '''
        for _ in range(n):
            face = random.choice('UDFBLR')
            dir  = random.choice('+-')
            self.move_face(face, dir)

    def scramble(self, nrots=10, nmoves=50):
        '''
        Scramble the cube.

        Arguments:
          nrots  -- number of random cube rotations to make
          nmoves -- number of random face moves to make

        Return value: none
        '''

        self.random_rotations(nrots)
        self.random_moves(nmoves)
        # Reset count before solving begins.
        self.count = 0

    def is_solved(self):
        '''
        Return True if the cube is solved.

        If the cube appears solved but is invalid, raise an
        InvalidCube exception with an appropriate error message.
        '''
        opposites = {'w' : 'y', 'y' : 'w', 'r' : 'o', 'o' : 'r', 'g' : 'b', 'b' : 'g'}
        faceColor = {}
        for f in ['U', 'D', 'F', 'B', 'L', 'R']:
            face = self.rep.get_face(f)
            colors = set(sum(face, []))
            if len(colors) != 1:
                return False
            faceColor[f] = colors.pop()
        if set(faceColor.values()) != {'w', 'y', 'g', 'b', 'r', 'o'}:
            raise InvalidCube("Not all colors represented on the cube.")
        if opposites[faceColor['U']] != faceColor['D']:
            raise InvalidCube("Top and bottom faces do not have a valid pair of colors.")
        elif opposites[faceColor['R']] != faceColor['L']:
            raise InvalidCube("Right and left faces do not have a valid pair of colors.")
        elif opposites[faceColor['F']] != faceColor['B']:
            raise InvalidCube("Front and back faces do not have a valid pair of colors.")
        else:
            ufrCombos = ['wgr', 'wrb', 'wbo', 'wog',
                         'goy', 'gyr', 'grw', 'gwo',
                         'ygo', 'yob', 'ybr', 'yrg',
                         'rwg', 'rgy', 'ryb', 'rbw',
                         'bwr', 'bry', 'byo', 'bow',
                         'owb', 'oby', 'oyg', 'ogw']
            last = self.rep.size - 1
            u = self.rep.get_face('U')[last][last]
            f = self.rep.get_face('F')[0][last]
            r = self.rep.get_face('R')[0][0]
            ufr = u + f + r
            if ufr not in ufrCombos:
                raise InvalidCube('U, F, and R faces in illegal configuration.')
            return True


    def display(self):
        '''
        Return a string version of the cube representation.
        '''

        return self.rep.display()

if __name__ == '__main__':
    cube = RubiksCube(3)
    cube.rep.test_faces()
    print(cube.display())
    # cube.scramble()
    # print(cube.display())
