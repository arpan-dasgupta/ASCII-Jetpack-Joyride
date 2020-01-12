import os
import sys
import time
import tty
import termios


SCREENHEIGHT = 31
SCREENWIDTH = 127
SLEEP_TIME = 0.215


def getchar():
    # Returns a single character from standard input
    file_desc = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_desc)
    try:
        tty.setraw(sys.stdin.fileno())
        charred = sys.stdin.read(1)
    finally:
        termios.tcsetattr(file_desc, termios.TCSADRAIN, old_settings)
    return charred


TIMER = 0
SCORE = 0
CUR_TIME = 0
MANUAL_MODE = 1
BOSS_MODE = 1


def reset():
    global TIMER
    global SCORE
    TIMER = 150
    SCORE = 0


def tick():
    global TIMER
    global CUR_TIME
    if TIMER > 0:
        if time.time() - CUR_TIME >= 1:
            TIMER -= 1
            CUR_TIME = time.time()
    return TIMER


def clear():
    # _ = os.system('clear')
    print('\033[0;0H')


if __name__ == "__main__":
    while True:
        print("press any key")
        CHARAC = getchar()
        print('You pressed')
        print(CHARAC)
        if CHARAC == 'q':
            sys.exit()
