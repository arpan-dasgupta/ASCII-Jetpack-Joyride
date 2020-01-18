from colorama import Fore
import numpy as np
from config import SCREENHEIGHT, SCREENWIDTH
from moving import Moving


class Magnet(Moving):

    def __init__(self, inipos):
        self.__magnet_range = 50
        self._posval = inipos

    def body(self):
        self.arr = np.full((5, 5, 1), 'M')
        self.arr[0, 2] = ' '
        self.arr[1, 2] = ' '
        self.arr[2, 2] = ' '
        self.arr[3, 2] = ' '
        self.msk = np.full((5, 5, 1), Fore.LIGHTBLACK_EX)
        return self.arr, self.msk

    def get_range(self):
        return self.__magnet_range


def magnet_spawner():
    # baseh = np.random.randint(int(SCREENHEIGHT*2/3), int(SCREENHEIGHT*5/6))
    # m = Magnet([int(SCREENHEIGHT/2), int(SCREENWIDTH/2)])
    baseh = np.random.randint(int(SCREENHEIGHT*2/3), int(SCREENHEIGHT*5/6))
    m = Magnet([baseh, SCREENWIDTH-11])
    return m
