import numpy as np
from colorama import Fore, Back
from moving import Moving


class Bullet(Moving):

    __bul_speed = 2

    def __init__(self, initpos):
        self._posval = initpos

    def body(self):
        array = np.array([[['-'], ['-'], ['-'], ['>']]])
        msk = np.full(np.shape(array), Back.WHITE)
        self._posval = self._posval
        return array, msk

    def update_pos(self):
        self._posval[1] += self.__bul_speed
