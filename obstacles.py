from moving import *
import numpy as np
from colorama import Fore, Back, Style
from config import *


class Straight_obstacle(Moving):

    aa = np.full((np.random.randint(4, 7), 1, 1), 'Z')
    msk = np.full(np.shape(aa), Fore.RED)

    def __init__(self, size, inipos):
        self.posval = inipos
        self.aa = np.full((size, 1, 1), 'Z')
        self.msk = np.full(np.shape(self.aa), Fore.RED)

    def body(self):
        return self.aa, self.msk
# c = Coins(5, [0, 0])
# print(c.get_val())
# print(c.get_pos())
# c.update_pos()
# print(c.get_pos())


def obstacle_gen():
    baseh = np.random.randint(int(screenheight/4), int(screenheight*3/4))
    obs = Straight_obstacle(np.random.randint(4, 7), [baseh, screenwidth-1])
    return obs
