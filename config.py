import os
import sys
import time
import tty
import termios


SCREENHEIGHT = 31
SCREENWIDTH = 147
SLEEP_TIME = 0.125


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
LIVES = 3
CUR_TIME = 0
MANUAL_MODE = 0
BOSS_MODE = 0
DRAGON_MODE = 2
SPEED_UP = 0
GROUNDWIDTH = 3
BOSS_THRESH = 50
BOSS_FIRE_RATE_PLAYER = 0.15
BOSS_FIRE_RATE_DRAGON = 0.5
SCENERY_GEN_RATE = 0.96
MAGNET_GEN_RATE = 0.02
OBSTACLE_GEN_RATE = 0.17
COIN_GEN_RATE = 0.04
RATE_CONTROL = 50000


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


def clear_2():
    _ = os.system('clear')
    # print('\033[0;0H')


BOSS_FIGHT = """888                                 .d888d8b        888     888    
888                                d88P" Y8P        888     888    
888                                888              888     888    
88888b.  .d88b. .d8888b .d8888b    888888888 .d88b. 88888b. 888888 
888 "88bd88""88b88K     88K        888   888d88P"88b888 "88b888    
888  888888  888"Y8888b."Y8888b.   888   888888  888888  888888    
888 d88PY88..88P     X88     X88   888   888Y88b 888888  888Y88b.  
88888P"  "Y88P"  88888P' 88888P'   888   888 "Y88888888  888 "Y888 
                                                 888               
                                            Y8b d88P               
                                             "Y88P"                """
GAME_OVER = """┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
"""
SCORE_INCREMENTOR = 5


if __name__ == "__main__":
    while True:
        print("press any key")
        CHARAC = getchar()
        print('You pressed')
        print(CHARAC)
        if CHARAC == 'q':
            sys.exit()
