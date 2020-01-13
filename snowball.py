from colorama import Fore
import numpy as np
from config import SCREENHEIGHT, SCREENWIDTH
from moving import Moving


class Snowball(Moving):

    cur_pos = [0, 0]
    bod = np.array([])
    mask = np.array([])
    diff = 0.6

    def __init__(self, pos):
        self.cur_pos = pos
        self.bod = np.array([[['_'], ['\\'], ['/'], ['_']],
                             [[' '], ['/'], ['\\'], [' ']]])
        self.mask = np.full(np.shape(self.bod), Fore.RED)

    def body(self):
        return self.bod, self.mask

    def get_pos(self):
        return self.cur_pos

    def update_pos(self, player_pos):
        self.cur_pos[1] -= 2
        if player_pos[0] < self.cur_pos[0]:
            self.cur_pos[0] -= (np.random.random_sample() < self.diff)
        elif player_pos[0] > self.cur_pos[0]+2:
            self.cur_pos[0] += (np.random.random_sample() < self.diff)
        if self.cur_pos[0] + 2 > SCREENHEIGHT:
            self.cur_pos[0] = SCREENHEIGHT - 2


if __name__ == "__main__":
    sn = Snowball([0, 0])
    a, _ = sn.body()

    for row in a:
        for c in row:
            print(c[0], end='')
        print()
