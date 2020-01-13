from colorama import Fore
import numpy as np
from bullet import Bullet
from config import SCREENWIDTH, SCREENHEIGHT
from person import Person


class Mandalorian(Person):

    dim = [5, 8]

    def attack(self):
        pass

    def attract(self, pos, range):
        if np.abs(pos[0]-self.cur_pos[0])+np.abs(pos[1]-self.cur_pos[1]) < range:
            ran = np.random.random_sample()
            new_a = np.subtract(pos, ran)
            ratio = new_a[0]/(new_a[0]+new_a[1]+0.001)
            # print(ratio, ran)
            # print(self.cur_pos, pos)
            if ran < ratio:
                self.cur_pos[1] += 4 * ((-1)**(pos[1] < self.cur_pos[1]))
            else:
                self.cur_pos[0] += 2 * ((-1)**(pos[0] < self.cur_pos[0]))
            # exit()
            # print(self.cur_pos)
            if self.cur_pos[0] < 0:
                self.cur_pos[0] = 0
            if self.cur_pos[1] < 0:
                self.cur_pos[1] = 0
            if self.cur_pos[0] > SCREENHEIGHT:
                self.cur_pos[0] = SCREENHEIGHT
            if self.cur_pos[1] > SCREENWIDTH:
                self.cur_pos[1] = SCREENWIDTH

    def return_pos(self):
        return self.cur_pos

    def move_up(self, val):
        self.cur_pos[0] = max(0, self.cur_pos[0]-val)

    def move_left(self, val):
        self.cur_pos[1] = max(0, self.cur_pos[1]-val)

    def move_down(self, val):
        self.cur_pos[0] = min(SCREENHEIGHT-self.dim[0], self.cur_pos[0]+val)

    def move_right(self, val):
        self.cur_pos[1] = min(SCREENWIDTH-self.dim[1], self.cur_pos[1]+val)

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
