import numpy as np
from colorama import Fore, Back
from moving import Moving


class Bullet(Moving):

    def __init__(self, initpos):
        self.posval = initpos

    def body(self):
        array = np.array([[['-'], ['-'], ['-'], ['>']]])
        msk = np.full(np.shape(array), Back.WHITE)
        self.posval = self.posval
        return array, msk

    def update_pos(self):
        self.posval[1] += 2
