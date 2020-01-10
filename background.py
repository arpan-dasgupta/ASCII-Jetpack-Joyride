import numpy as np
from colorama import Fore, Back, Style


class Screen:

    screenheight = 31
    screenwidth = 127
    color_mask = np.full((screenheight, screenwidth, 1), Fore.RED)
    matrix = np.full((screenheight, screenwidth, 1), ' ')
    background_color = Back.BLUE

    def __init__(self):
        pass

    def addToScreen(self, obj, cm, start):
        self.matrix[start[0]:start[0] +
                    np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = obj
        self.color_mask[start[0]:start[0] +
                        np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = cm

    def printscreen(self):
        print(self.background_color + Style.BRIGHT, end='')
        for i in range(self.screenheight):
            for j in range(self.screenwidth):
                print(self.color_mask[i][j][0] + self.matrix[i][j][0], end='')
            print()

    def clrscr(self):
        self.matrix = np.full((self.screenheight, self.screenwidth, 1), ' ')
        self.color_mask = np.full(
            (self.screenheight, self.screenwidth, 1), Fore.RED)


# sc = Screen()
# sc.addToScreen([])
# sc.printscreen()
