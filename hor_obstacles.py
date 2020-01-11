from moving import *
import numpy as np
from colorama import Fore, Back, Style
from config import *
from obstacles import *
from diag_obstacles import *


class Hor_obstacle(Obstacle):

    def __init__(self, size, inipos):
        self.posval = inipos
        self.aa = np.full((1, size, 1), 'Z')
        self.msk = np.full(np.shape(self.aa), Fore.RED)


def obstacle_gen():
    baseh = np.random.randint(int(screenheight/4), int(screenheight*3/4))
    kk = np.random.randint(0, 3)
    if kk == 1:
        obs = Obstacle(np.random.randint(4, 7), [baseh, screenwidth-1])
    elif kk == 0:
        obs = Diag_obstacle(np.random.randint(
            4, 7), [baseh, screenwidth-8], np.random.randint(0, 2))
    else:
        obs = Hor_obstacle(np.random.randint(7, 10), [baseh, screenwidth-11])

    return obs
