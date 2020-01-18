from colorama import Fore
import numpy as np
from config import SCREENHEIGHT, SCREENWIDTH
from diag_obstacles import DiagObstacle
from obstacles import Obstacle


class HorObstacle(Obstacle):

    def __init__(self, size, inipos):
        self._posval = inipos
        self._array = np.full((1, size, 1), '#')
        self._msk = np.full(np.shape(self._array), Fore.RED)


def obstacle_gen():
    max_height = 7
    baseh = np.random.randint(0, SCREENHEIGHT - max_height)
    key_val = np.random.randint(0, 3)
    if key_val == 1:
        obs = Obstacle(np.random.randint(4, 7), [baseh, SCREENWIDTH-1])
    elif key_val == 0:
        obs = DiagObstacle(np.random.randint(
            4, 7), [baseh, SCREENWIDTH-8], np.random.randint(0, 2))
        # fd = open("log.txt", 'a')
        # fd.write(str(obs)+'\n')
        # fd.close()
    else:
        obs = HorObstacle(np.random.randint(7, 10), [baseh, SCREENWIDTH-11])

    return obs
