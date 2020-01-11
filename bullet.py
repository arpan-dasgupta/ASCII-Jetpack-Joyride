from config import *
import numpy as np
from colorama import Fore, Back, Style
from moving import Moving


class Bullet(Moving):

    def __init__(self, initpos):
        self.posval = initpos

    def body(self):
        aa = np.array([[['-'], ['-'], ['-'], ['>']]])
        msk = np.full(np.shape(aa), Fore.GREEN)
        return aa, msk

    def update_pos(self):
        self.posval[1] += 2
