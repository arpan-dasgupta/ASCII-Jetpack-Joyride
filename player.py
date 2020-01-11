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

    def attract(self, pos, range):
        if np.abs(pos[0]-self.curpos[0])+np.abs(pos[1]-self.curpos[1]) < range:
            ran = np.random.random_sample()
            new_a = np.subtract(pos, ran)
            ratio = new_a[0]/(new_a[0]+new_a[1]+0.001)
            # print(ratio, ran)
            # print(self.curpos, pos)
            if ran < ratio:
                self.curpos[1] += 4 * ((-1)**(pos[1] < self.curpos[1]))
            else:
                self.curpos[0] += 2 * ((-1)**(pos[0] < self.curpos[0]))
            # exit()
            # print(self.curpos)
            if self.curpos[0] < 0:
                self.curpos[0] = 0
            if self.curpos[1] < 0:
                self.curpos[1] = 0
            if self.curpos[0] > SCREENHEIGHT:
                self.curpos[0] = SCREENHEIGHT
            if self.curpos[1] > SCREENWIDTH:
                self.curpos[1] = SCREENWIDTH

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
