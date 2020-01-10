import os
from kbhit import *
import random
from colorama import Fore, Back, Style
import time
import tty
import termios
import sys


screenheight = 31
screenwidth = 127
sleep_time = 0.215


def getchar():
    # Returns a single character from standard input
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


timer = 0
score = 0


def tick():
    global timer
    global cur_time
    if (timer > 0):
        if time.time() - cur_time >= 1:
            timer -= 1
            cur_time = time.time()
    return timer


def clear():
    _ = os.system('clear')


if __name__ == "__main__":
    while(True):
        print("press any key")
        ch = getchar()
        print('You pressed')
        print(ch)
        if(ch == 'q'):
            exit(0)
