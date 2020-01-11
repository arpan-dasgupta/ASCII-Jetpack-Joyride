import numpy as np
from colorama import Fore, Back, Style
from config import SCREENWIDTH, SCREENHEIGHT


class Screen:

    color_mask = np.full((SCREENHEIGHT, SCREENWIDTH, 1), Fore.RED)
    matrix = np.full((SCREENHEIGHT, SCREENWIDTH, 1), ' ')
    background_color = Back.BLUE

    def __init__(self):
        pass

    def add_to_screen(self, obj, col_m, start):
        self.matrix[start[0]:start[0] +
                    np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = obj
        self.color_mask[start[0]:start[0] +
                        np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = col_m

    def printscreen(self):
        print(self.background_color + Style.BRIGHT, end='')
        for i in range(SCREENHEIGHT):
            for j in range(SCREENWIDTH):
                print(self.color_mask[i][j][0] + self.matrix[i][j][0], end='')
            print()

    def clrscr(self):
        self.matrix = np.full((SCREENHEIGHT, SCREENWIDTH, 1), ' ')
        self.color_mask = np.full(
            (SCREENHEIGHT, SCREENWIDTH, 1), Fore.RED)


# sc = Screen()
# sc.add_to_screen([])
# sc.printscreen()
