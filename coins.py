from colorama import Fore
import numpy as np
from config import SCREENHEIGHT, SCREENWIDTH
from moving import Moving


class Coins(Moving):

    def __init__(self, value, inipos):
        self._posval = inipos
        self.__coinval = value

    def get_val(self):
        return self.__coinval

    def body(self):
        array = np.full((1, 1, 1), '*')
        msk = np.full(np.shape(array), Fore.BLACK)
        self.__coinval = self.__coinval
        return array, msk
# c = Coins(5, [0, 0])
# print(c.get_val())
# print(c.get_pos())
# c.update_pos()
# print(c.get_pos())


def random_coin_gen():
    new_c = []
    baseh = np.random.randint(int(SCREENHEIGHT/4), int(SCREENHEIGHT*3/4))
    coin_height = np.random.randint(3, 7)
    coin_width = np.random.randint(4, 6)
    for i in range(coin_height):
        for j in range(coin_width):
            basew = SCREENWIDTH - 11
            coin_obj = Coins(1, [baseh+i, basew+j])
            new_c.append(coin_obj)
    return new_c
