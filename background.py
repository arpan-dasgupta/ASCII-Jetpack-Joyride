import numpy as np
from colorama import Fore, Back, Style
from config import SCREENWIDTH, SCREENHEIGHT, SCORE, TIMER
import config


class Screen:

    color_mask = np.full((SCREENHEIGHT+5, SCREENWIDTH, 1), Fore.RED)
    matrix = np.full((SCREENHEIGHT+5, SCREENWIDTH, 1), ' ')
    background_color = Back.LIGHTCYAN_EX

    def __init__(self):
        lower = np.full((5, SCREENWIDTH, 1), Back.GREEN)
        self.color_mask[SCREENHEIGHT:, :, :] = lower

    def add_to_screen(self, obj, col_m, start):
        self.matrix[start[0]:start[0] +
                    np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = obj
        self.color_mask[start[0]:start[0] +
                        np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = col_m

    def printscreen(self):
        print(Style.BRIGHT, end='')
        to_print = ""
        for i in range(SCREENHEIGHT+5):
            for j in range(SCREENWIDTH):
                to_print += (self.background_color + self.color_mask[i][j][0] + self.matrix[i]
                             [j][0] + Style.RESET_ALL)
            to_print += '\n'
        to_print += ("Score - "+str(config.SCORE) +
                     "\n TIME - " + str(config.TIMER) + "\n Lives - " + str(config.LIVES)+"\n")
        print(to_print)

    def clrscr(self):
        self.matrix = np.full((SCREENHEIGHT+5, SCREENWIDTH, 1), ' ')
        self.color_mask = np.full(
            (SCREENHEIGHT+5, SCREENWIDTH, 1), Fore.RED)
        lower = np.full((5, SCREENWIDTH, 1), Back.GREEN)
        self.color_mask[SCREENHEIGHT:, :, :] = lower


# sc = Screen()
# sc.add_to_screen([])
# sc.printscreen()
