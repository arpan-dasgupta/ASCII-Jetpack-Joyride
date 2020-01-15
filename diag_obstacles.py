from colorama import Fore
import numpy as np
from moving import Moving
from obstacles import Obstacle
import config


class DiagObstacle(Moving):

    ele = []
    size = 0

    def __init__(self, size, inipos, direction):
        self.size = size
        self.posval = inipos
        self.ele = []
        for i in range(size):
            if direction == 1:
                obj = Obstacle(1, [inipos[0]+i, inipos[1]+i])
            else:
                obj = Obstacle(1, [inipos[0]+size-1-i, inipos[1]+i])
            self.ele.append(obj)
        self.array = np.full((size, 1, 1), '#')
        self.msk = np.full(np.shape(self.array), Fore.RED)

    def update_pos(self):
        # print(self.posval, self.posval[1] -
        #       self.ele[0].get_pos()[1], len(self.ele))
        self.posval[1] -= 2 + 2 * (config.SPEED_UP == 1)
        for element in self.ele:
            element.update_pos()

    def body(self):
        lli = []
        for array in self.ele:
            good = array.body()
            lli.append(good[0])
        return lli

    def del_ob(self):
        for elem in self.ele:
            del elem
