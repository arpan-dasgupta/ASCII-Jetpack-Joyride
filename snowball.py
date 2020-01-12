from colorama import Fore
import numpy as np


class Snowball:

    cur_pos = [0, 0]
    bod = np.array([])
    mask = np.array([])

    def __init__(self, pos):
        self.cur_pos = pos
        self.bod = np.array([[['_'], ['\\'], ['/'], ['_']],
                             [[' '], ['/'], ['\\'], [' ']]])
        self.mask = np.full(np.shape(self.bod), Fore.RED)

    def body(self):
        return self.body, self.mask

    def get_pos(self):
        return self.cur_pos
