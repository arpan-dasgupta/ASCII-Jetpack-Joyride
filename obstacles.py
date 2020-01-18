from colorama import Fore
import numpy as np
from moving import Moving


class Obstacle(Moving):

    _array = np.full((np.random.randint(4, 7), 1, 1), '#')
    _msk = np.full(np.shape(_array), Fore.RED)

    def __init__(self, size, inipos):
        self._posval = inipos
        self._array = np.full((size, 1, 1), '#')
        self._msk = np.full(np.shape(self._array), Fore.RED)

    def body(self):
        return [[self._array, self._msk, self._posval]]
