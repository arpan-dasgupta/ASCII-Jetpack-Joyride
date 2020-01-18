import numpy as np
from colorama import Fore, Back, Style
from config import SCREENWIDTH, SCREENHEIGHT, SCORE, TIMER
import config


class Screen:

    __color_mask = np.full((SCREENHEIGHT+3, SCREENWIDTH, 1), Fore.RED)
    __matrix = np.full((SCREENHEIGHT+3, SCREENWIDTH, 1), ' ')
    __background_color = Back.LIGHTCYAN_EX

    def __init__(self):
        lower = np.full((3, SCREENWIDTH, 1), Back.GREEN)
        self.__color_mask[SCREENHEIGHT:, :, :] = lower

    def add_to_screen(self, obj, col_m, start, overload=None):
        if overload == None:
            self.__matrix[start[0]:start[0] +
                          np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = obj
            self.__color_mask[start[0]:start[0] +
                              np.shape(obj)[0], start[1]:start[1]+np.shape(obj)[1]] = col_m
        else:
            # print(SCREENWIDTH, start, np.shape(obj), max(
            #     start[1], 0), start[1]+np.shape(obj)[1])
            self.__matrix[start[0]:start[0] +
                          np.shape(obj)[0], max(start[1], 0):start[1]+np.shape(obj)[1]] = obj[:, max(0, -start[1]):min(np.shape(obj)[1], SCREENWIDTH-start[1])]
            self.__color_mask[start[0]:start[0] +
                              np.shape(obj)[0], max(start[1], 0):start[1]+np.shape(obj)[1]] = col_m[:, max(0, -start[1]):min(np.shape(obj)[1], SCREENWIDTH-start[1])]
            # self.__matrix[np.max(start[0], 0):np.max(np.min(start[0] +
            #                                               np.shape(obj)[0], SCREENHEIGHT), 0), np.max(start[1], 0):np.max(np.min(start[1] + np.shape(obj)[1], SCREENWIDTH), 0)] = obj[:, max(0, -start[0]):min(np.shape(obj)[0], SCREENWIDTH-start[1])]
            # self.__color_mask[np.max(start[0], 0):np.max(np.min(start[0] +
            #                                                   np.shape(obj)[0], SCREENHEIGHT), 0), np.max(start[1], 0):np.max(np.min(start[1] + np.shape(obj)[1], SCREENWIDTH), 0)] = col_m[:, max(0, -start[0]):min(np.shape(obj)[0], SCREENWIDTH-start[1])]

    def printscreen(self, shield_status):
        print(Style.BRIGHT, end='')
        to_print = ""
        for i in range(SCREENHEIGHT+3):
            for j in range(SCREENWIDTH):
                to_print += (self.__background_color + self.__color_mask[i][j][0] + self.__matrix[i]
                             [j][0] + Style.RESET_ALL)
            to_print += '\n'
        to_print += ("Score - "+str(config.SCORE) +
                     "\t TIME - " + str(config.TIMER) + "\t Lives - " + str(config.LIVES)+"\t")
        if shield_status[0] == 1:
            to_print += ("Shield active for time -  " +
                         str(shield_status[1]) + '\t')
        else:
            to_print += ("Cooldown time for shield - " +
                         str(shield_status[1]) + '\t')
        if config.SPEED_UP:
            to_print += ("SPEED BOOST - ACTIVE  \n")
        else:
            to_print += ("SPEED BOOST - INACTIVE\n")

        # to_print += ("[")
        # for i in range(20):
        #     if boss_lives > i:
        #         to_print += ("#")
        #     else:
        #         to_print += (" ")

        # to_print += ("]\n")
        print(to_print)

    def clrscr(self):
        self.__matrix = np.full((SCREENHEIGHT+3, SCREENWIDTH, 1), ' ')
        self.__color_mask = np.full(
            (SCREENHEIGHT+3, SCREENWIDTH, 1), Fore.RED)
        lower = np.full((3, SCREENWIDTH, 1), Back.GREEN)
        self.__color_mask[SCREENHEIGHT:, :, :] = lower


# sc = Screen()
# sc.add_to_screen([])
# sc.printscreen()
