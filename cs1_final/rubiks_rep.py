# Name: Maxwell Vale
# Login: mvale
'''
Rubik's cube representations and basic operations.
'''

import rubiks_utils as u
import copy

class RubiksRep:
    '''
    Basic functionality of Rubik's cubes.
    '''
    def __init__(self, size):
        '''
        Initialize the cube representation.
        '''
        assert size > 0
        self.size = size
        self.contents = {}
        sides = [('U', 'w'), ('D', 'y'), ('F', 'r'), ('B', 'o'), ('L', 'g'), ('R', 'b')]
        for face, color in sides:
            faceList = []
            for i in range(size):
                faceList.append(list(color) * size)
            self.contents[face] = faceList

    ### Accessors.

    def get_row(self, face, row):
        '''
        Return a copy of the indicated row on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert row >= 0 and row < self.size
        return self.contents[face][row][:]

    def get_col(self, face, col):
        '''
        Return a copy of the indicated column on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert col >= 0 and col < self.size
        c = []
        for row in self.contents[face]:
            c.append(row[col])
        return c

    def set_row(self, face, row, values):
        '''
        Change the contents of the indicated row on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert row >= 0 and row < self.size
        assert type(values) is list
        assert len(values) == self.size
        self.contents[face][row] = values[:]

    def set_col(self, face, col, values):
        '''
        Change the contents of the indicated column on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert col >= 0 and col < self.size
        assert type(values) is list
        assert len(values) == self.size
        for i in range(self.size):
            self.contents[face][i][col] = values[i]

    def get_face(self, face):
        '''
        Return the colors of a face, as a list of lists.
        '''
        assert face in self.contents
        return copy.deepcopy(self.contents[face])

    ### Basic operations.

    def rotate_face_cw(self, face):
        '''
        Rotate a 3x3 face clockwise.
        '''

        assert face in self.contents
        cw = []
        for i in range(self.size):
            cw.append(self.get_col(face, i))
        self.contents[face] = [x[::-1] for x in cw]

    def rotate_face_ccw(self, face):
        '''
        Rotate a 3x3 face counterclockwise.
        '''

        assert face in self.contents
        ccw = []
        for i in range(self.size):
            ccw.append(self.get_col(face, i))
        self.contents[face] = ccw[::-1]

    def move_F(self):
        '''
        Move the F face one-quarter turn clockwise.
        '''
        last = self.size - 1
        self.rotate_face_cw('F')
        temp = self.get_row('U', last)
        self.set_row('U', last, self.get_col('L', last)[::-1])
        self.set_col('L', last, self.get_row('D', 0))
        self.set_row('D', 0, self.get_col('R', 0)[::-1])
        self.set_col('R', 0, temp)

    def rotate_cube_X(self):
        '''
        Rotate the cube in the positive X direction.
        '''
        U = self.get_face('U')
        self.contents['U'] = self.get_face('F')
        self.contents['F'] = self.get_face('D')
        self.contents['D'] = self.get_face('B')
        self.contents['B'] = U
        self.rotate_face_cw('R')
        self.rotate_face_ccw('L')

    def rotate_cube_Y(self):
        '''
        Rotate the cube in the positive Y direction.
        '''
        B = [x[::-1] for x in self.get_face('B')[::-1]]
        self.contents['B'] = [x[::-1] for x in self.get_face('L')[::-1]]
        self.contents['L'] = self.get_face('F')
        self.contents['F'] = self.get_face('R')
        self.contents['R'] = B
        self.rotate_face_cw('U')
        self.rotate_face_ccw('D')


    def rotate_cube_Z(self):
        '''
        Rotate the cube in the positive Z direction.
        '''
        self.rotate_cube_X()
        self.rotate_cube_Y()
        self.rotate_cube_X()
        self.rotate_cube_X()
        self.rotate_cube_X()


    def display(self):
        '''
        Return a string version of the cube representation.
        '''

        return u.display(self.contents, self.size)

    def test_faces(self):
        '''
        Load the representation with unique characters.  For testing.
        '''

        self.contents = u.test_faces(self.size)

if __name__ == '__main__':
    rep = RubiksRep(3)
    rep.test_faces()
    print(rep.display())
    rep.rotate_cube_Z()
    print(rep.display())
