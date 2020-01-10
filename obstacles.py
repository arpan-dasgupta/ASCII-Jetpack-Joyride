from moving import *
import numpy as np
from colorama import Fore, Back, Style
from config import *


class Straight_obstacle(Moving):

    coinval = 0

    def __init__(self, value, inipos):
        self.posval = inipos
        self.coinval = value

    def get_val(self):
        return self.coinval

    def body(self):
        aa = np.full((np.random.randn(1, 2), 1, 1), '*')
        msk = np.full(np.shape(aa), Fore.BLACK)
        return aa, msk
# c = Coins(5, [0, 0])
# print(c.get_val())
# print(c.get_pos())
# c.update_pos()
# print(c.get_pos())


def random_coin_gen():
    new_c = []
    baseh = np.random.randint(int(screenheight/4), int(screenheight*3/4))
    ch = np.random.randint(3, 7)
    cw = np.random.randint(4, 6)
    for i in range(ch):
        for j in range(cw):
            basew = screenwidth - cw - 1
            cc = Coins(1, [baseh+i, basew+j])
            new_c.append(cc)
    return new_c
