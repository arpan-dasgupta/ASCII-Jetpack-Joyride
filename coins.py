from moving import *
import numpy as np
from colorama import Fore, Back, Style


class Coins(Moving):

    coinval = 0

    def __init__(self, value, inipos):
        self.posval = inipos
        self.coinval = value

    def get_val(self):
        return self.coinval

    def body(self):
        aa = np.full((1, 1, 1), '@')
        msk = np.full(np.shape(aa), Fore.YELLOW)
        return aa, msk
# c = Coins(5, [0, 0])
# print(c.get_val())
# print(c.get_pos())
# c.update_pos()
# print(c.get_pos())


def random_coin_gen():
    new_c = []
    new_cm = []
    for i in range(np.random.randint(3, 7)):
        for j in range(np.random.randint(4, 6)):
            # cc = Coins(1,)
            pass
    return new_c, new_cm
