from colorama import Fore
import numpy as np
from bullet import Bullet
from config import SCREENWIDTH, SCREENHEIGHT
from person import Person


class Mandalorian(Person):

    curpos = [0, 30]
    dim = [5, 8]

    def shoot(self):
        bullet = Bullet(self.curpos.copy())
        return bullet

    def attack(self):
        pass

    def return_pos(self):
        return self.curpos

    def move_up(self, val):
        self.curpos[0] = max(0, self.curpos[0]-val)

    def move_left(self, val):
        self.curpos[1] = max(0, self.curpos[1]-val)

    def move_down(self, val):
        self.curpos[0] = min(SCREENHEIGHT-self.dim[0], self.curpos[0]+val)

    def move_right(self, val):
        self.curpos[1] = min(SCREENWIDTH-self.dim[1], self.curpos[1]+val)

    def body(self):
        array = np.array([[[' '],
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
        msk = np.full(np.shape(array), Fore.RED)
        return array, msk
