from colorama import Fore
import numpy as np
from moving import Moving


class Obstacle(Moving):

    array = np.full((np.random.randint(4, 7), 1, 1), '#')
    msk = np.full(np.shape(array), Fore.RED)

    def __init__(self, size, inipos):
        self._posval = inipos
        self.array = np.full((size, 1, 1), '#')
        self.msk = np.full(np.shape(self.array), Fore.RED)

    def body(self):
        return [[self.array, self.msk, self._posval]]
