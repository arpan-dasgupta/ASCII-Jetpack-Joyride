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


def update_objects(p, coins):
    p.move_down(1)
    for coin in coins:
        coin.update_pos()


def render_objects(scr, bd, msk, p, coins):
    to_rem_c = []
    i = 0
    for coin in coins:
        if(coin.get_pos()[1] <= 0):
            to_rem_c.append(coin)
            continue
        f1, f2 = coin.body()
        scr.addToScreen(f1, f2, coin.get_pos())
        i += 1
    for a in to_rem_c:
        coins.remove(a)
        del a
    pos = p.return_pos()
    scr.addToScreen(bd, msk, pos)
    scr.printscreen()


def main():
    scr = Screen()
    # lives = 3
    playing = 1
    coins_collected = 0
    died = 0

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
            update_objects(p, coins)
            if np.random.randint(0, 100) < 4:
                new_c = random_coin_gen()
                coins.extend(new_c)
            render_objects(scr, bd, msk, p, coins)
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
