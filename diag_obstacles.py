from moving import *
import numpy as np
from colorama import Fore, Back, Style
from config import *
from obstacles import *


class Diag_obstacle(Moving):

    ele = []
    size = 0

    def __init__(self, size, inipos, dir):
        self.size = size
        self.posval = inipos
        for i in range(size):
            if dir == 1:
                o = Obstacle(1, [inipos[0]+i, inipos[1]+i])
            else:
                o = Obstacle(1, [inipos[0]+size-1+i, inipos[1]+i])
            self.ele.append(o)
        self.aa = np.full((size, 1, 1), 'Z')
        self.msk = np.full(np.shape(self.aa), Fore.RED)

    def update_pos(self):
        for e in self.ele:
            e.update_pos()

    def body(self):
        lli = []
        for a in self.ele:
            g1 = a.body()
            lli.append(g1[0])
        return lli
