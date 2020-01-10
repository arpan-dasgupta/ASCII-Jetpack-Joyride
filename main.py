from player import *
from background import *
from kbhit import *
import termios
import time
import copy
import signal
import tty
import sys
from config import *
from coins import *


def destroy(p):
    del p


def reset():
    global timer
    global score
    timer = 150
    score = 0


def render_objects(scr, bd, msk, p, coins, coins_mask):
    pos = p.return_pos()
    scr.addToScreen(bd, msk, pos)


def main():
    scr = Screen()
    # lives = 3
    playing = 1
    coins_collected = 0
    died = 0
    sleep_time = 0.215

    while(playing == 1):
        if died == 1:
            # if lives != 0:
            #     died = 0
            #     destroy(p)
            #     time.sleep(2)
            #     # create_map()
            # else:
            clear()
            print(Back.WHITE + Fore.BLACK + "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n")
            exit()
        p = Mandalorian()
        keypress = KBHit()
        bd, msk = p.body()
        pos = p.return_pos()
        coins = []
        coins_mask = []
        scr.addToScreen(bd, msk, pos)
        while(True):
            tick()
            if keypress.kbhit():
                ch = keypress.getch()
                if ch == 'w':
                    p.move_up(3)
                elif ch == 's':
                    p.move_down(1)
                elif ch == 'a':
                    p.move_left(3)
                elif ch == 'd':
                    p.move_right(3)
                else:
                    died = 1
                    break
            clear()
            scr.clrscr()
            new_c, new_cm = random_coin_gen()
            render_objects(scr, bd, msk, p, coins, coins_mask)
            p.move_down(1)
            scr.printscreen()
            time.sleep(sleep_time)


if __name__ == '__main__':
    main()

# scr = Screen()
# guy = Mandalorian()
# guy.move_down(20)
# bd = guy.body()
# scr.addToScreen(bd, np.full(np.shape(bd), Fore.BLUE), guy.return_pos())
# scr.printscreen()
# clear()
