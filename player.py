from person import Person
import numpy as np
from colorama import Fore, Back, Style
from config import *


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

    def move_left(self, val):
        self.curpos[1] = max(0, self.curpos[1]-val)

    def move_down(self, val):
        self.curpos[0] = min(screenheight-self.dim[0], self.curpos[0]+val)

    def move_right(self, val):
        self.curpos[1] = min(screenwidth-self.dim[1], self.curpos[1]+val)

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
        msk = np.full(np.shape(aa), Fore.RED)
        return aa, msk
