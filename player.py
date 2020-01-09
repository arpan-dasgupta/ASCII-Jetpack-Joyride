from person import Person
import numpy as np

screenheight = 31
screenwidth = 127


class Mandalorian(Person):

    curpos = [0, 30]
    dim = [5, 8]

    def shoot(self):
        pass

    def attack(self):
        pass

    def return_pos(self):
        return self.curpos

    def move_up(self, val):
        self.curpos[0] = max(0, self.curpos[0]-val)

    def move_down(self, val):
        self.curpos[0] = min(screenheight-self.dim[0], self.curpos[0]+val)

    def body(self):
        aa = np.array([[[' '],
                        [' '],
                        [' '],
                        ['='],
                        ['='],
                        [' '],
                        [' '],
                        [' ']],
                       [['<'],
                        ['^'],
                        ['\\'],
                        ['('],
                        [')'],
                        ['/'],
                        ['^'],
                        ['>']],
                       [[' '],
                        ['\\'],
                        ['/'],
                        [' '],
                        [' '],
                        ['\\'],
                        ['/'],
                        [' ']
                        ],
                       [[' '],
                        [' '],
                        ['/'],
                        [' '],
                        [' '],
                        ['\\'],
                        [' '],
                        [' ']],
                       [[' '],
                        [' '],
                        ['`'],
                        ['\''],
                        ['\''],
                        ['`'],
                        [' '],
                        [' '],
                        ]])
        return aa
