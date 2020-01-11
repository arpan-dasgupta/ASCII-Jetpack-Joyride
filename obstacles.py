from moving import *
import numpy as np
from colorama import Fore, Back, Style
from config import *


class Obstacle(Moving):

    aa = np.full((np.random.randint(4, 7), 1, 1), 'Z')
    msk = np.full(np.shape(aa), Fore.RED)

    def __init__(self, size, inipos):
        self.posval = inipos
        self.aa = np.full((size, 1, 1), 'Z')
        self.msk = np.full(np.shape(self.aa), Fore.RED)

    def body(self):
        return [[self.aa, self.msk, self.posval]]
