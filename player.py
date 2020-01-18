from colorama import Fore, Back
import numpy as np
from bullet import Bullet
from config import SCREENWIDTH, SCREENHEIGHT
from person import Person
import config


class Mandalorian(Person):

    __dim = [5, 8]
    __velocity = [0, 0]
    __shield_timer = 20
    __shield_activated = 0
    __shield_timer = 20
    __shield_cooldown = 300

    def __init__(self):
        self._cur_pos = [0, 0]
        self.__shield_cooldown = 10
        self.__shield_timer = 0

    def attack(self):
        pass

    def attract(self, pos, range):
        if np.abs(pos[0]-self._cur_pos[0])+np.abs(pos[1]-self._cur_pos[1]) < range:
            ran = np.random.random_sample()
            new_a = np.subtract(pos, ran)
            ratio = new_a[0]/(new_a[0]+new_a[1]+0.001)
            # print(ratio, ran)
            # print(self._cur_pos, pos)
            if ran < ratio:
                self._cur_pos[1] += 4 * ((-1)**(pos[1] < self._cur_pos[1]))
            else:
                self._cur_pos[0] += 2 * ((-1)**(pos[0] < self._cur_pos[0]))
            # exit()
            # print(self._cur_pos)
            if self._cur_pos[0] < 0:
                self._cur_pos[0] = 0
            if self._cur_pos[1] < 0:
                self._cur_pos[1] = 0
            if self._cur_pos[0] > SCREENHEIGHT:
                self._cur_pos[0] = SCREENHEIGHT
            if self._cur_pos[1] > SCREENWIDTH:
                self._cur_pos[1] = SCREENWIDTH

    def return_pos(self):
        return self._cur_pos

    def shield_activate(self):
        if self.__shield_cooldown != 0:
            return
        self.__shield_timer = 60
        self.__shield_activated = 1

    def shield_status(self):
        return [self.__shield_activated, self.__shield_cooldown if not self.__shield_activated else self.__shield_timer]

    def shield_deactivate(self):
        self.__shield_timer = 6

    def update_pos(self):
        self._cur_pos[0] = max(0, min(SCREENHEIGHT-self.__dim[0],
                                      self._cur_pos[0]+self.__velocity[0]))
        if self._cur_pos[0] == SCREENHEIGHT-self.__dim[0] or self._cur_pos == 0:
            self.__velocity[0] = 0
        self.__velocity[0] += 1
        if self.__shield_timer == 0:
            self.__shield_cooldown = max(self.__shield_cooldown-1, 0)
            self.__shield_activated = 0
        else:
            self.__shield_timer -= 1
            if self.__shield_timer == 0:
                self.__shield_cooldown = 50
                self.__shield_activated = 0
        if self.__shield_timer == 0:
            config.SPEED_UP = 0
        else:
            self.__shield_timer -= 1

    def speed_up(self):
        config.SPEED_UP = 1
        self.__shield_timer = 20

    def move_up(self, val):
        self.__velocity[0] -= val
        # self._cur_pos[0] = max(0, self._cur_pos[0]-val)

    def move_left(self, val):
        self._cur_pos[1] = max(0, self._cur_pos[1]-val)

    def move_down(self, val):
        self.__velocity[0] += val
        # self._cur_pos[0] = min(SCREENHEIGHT-self.__dim[0], self._cur_pos[0]+val)

    def move_right(self, val):
        self._cur_pos[1] = min(SCREENWIDTH-self.__dim[1], self._cur_pos[1]+val)

    def body(self):
        array = np.array([[[' '],
                           [' '],
                           [' '],
                           ['='],
                           ['='],
                           [' '],
                           [' '],
                           [' ']],
                          [['<'],
                           ['^'],
                           ['\\'],
                           ['('],
                           [')'],
                           ['/'],
                           ['^'],
                           ['>']],
                          [[' '],
                           ['\\'],
                           ['/'],
                           [' '],
                           [' '],
                           ['\\'],
                           ['/'],
                           [' ']
                           ],
                          [[' '],
                           [' '],
                           ['/'],
                           [' '],
                           [' '],
                           ['\\'],
                           [' '],
                           [' ']],
                          [[' '],
                           [' '],
                           ['`'],
                           ['\''],
                           ['\''],
                           ['`'],
                           [' '],
                           [' '],
                           ]])
        if self.__shield_activated == 1:
            msk = np.full(np.shape(array), Back.BLACK + Fore.WHITE)
        elif config.SPEED_UP:
            msk = np.full(np.shape(array), Back.RED)
        else:
            msk = np.full(np.shape(array), Fore.BLACK)
        return array, msk
