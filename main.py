import sys
import time
from colorama import Fore, Back
import numpy as np
from background import Screen
from boss import Boss
from coins import random_coin_gen
from collision import collision_checker
from config import clear, tick, SLEEP_TIME, reset, SCORE, MANUAL_MODE, BOSS_MODE
from hor_obstacles import obstacle_gen
from kbhit import KBHit
from magnet import Magnet, magnet_spawner
from player import Mandalorian, SCREENWIDTH
from snowball import Snowball


def check_collisions(per, obstacles, magnets, coins, bullets, boss, snowballs):
    global SCORE
    to_rem_o = []
    for obstacle in obstacles:
        flag = 0
        for bullet in bullets:
            if flag == 1:
                break
            obs = obstacle.body()
            part3, _ = bullet.body()
            for indiv in obs:
                part1, _, pos = indiv
                if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                        np.shape(part3)[0], np.shape(part3)[1]], pos, bullet.get_pos()):
                    flag = 1
                    break
        if flag == 1:
            to_rem_o.append(obstacle)
    for obj in to_rem_o:
        obstacles.remove(obj)
    for obstacle in obstacles:
        obs = obstacle.body()
        part3, _ = per.body()
        for indiv in obs:
            part1, _, pos = indiv
            if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                    np.shape(part3)[0], np.shape(part3)[1]], pos, per.return_pos()):
                exit()
    to_rem_c = []
    part3, _ = per.body()
    for coin in coins:
        if collision_checker([np.shape(part3)[0], np.shape(part3)[1]], [1, 1],  per.return_pos(), coin.get_pos()):
            to_rem_c.append(coin)
            SCORE += coin.get_val()
    for coin in to_rem_c:
        coins.remove(coin)


def update_objects(per, coins, obstacles, bullets, magnets, boss, snowballs):
    per.move_down(1)
    for coin in coins:
        coin.update_pos()
    for obs in obstacles:
        obs.update_pos()
    for bul in bullets:
        bul.update_pos()
    for snowball in snowballs:
        snowball.update_pos(per.return_pos())
    for mag in magnets:
        mag.update_pos()
        per.attract(mag.get_pos(), mag.get_range())
    boss.update_pos(per.return_pos())


def render_objects(scr, bod, msk, per, coins, obstacle, bullets, magnets, boss, snowballs):
    to_rem_c = []
    to_rem_o = []
    to_rem_m = []
    to_rem_s = []
    i = 0
    for coin in coins:
        if coin.get_pos()[1] <= 0:
            to_rem_c.append(coin)
            continue
        f_f1, f_f2 = coin.body()
        scr.add_to_screen(f_f1, f_f2, coin.get_pos())
        i += 1
    for a_a in to_rem_c:
        coins.remove(a_a)
        del a_a
    i = 0
    for magnet in magnets:
        if magnet.get_pos()[1] <= 0:
            to_rem_m.append(magnet)
            continue
        f_f1, f_f2 = magnet.body()
        scr.add_to_screen(f_f1, f_f2, magnet.get_pos())
        i += 1
    for a_a in to_rem_m:
        magnets.remove(a_a)
        del a_a
    pos = per.return_pos()
    scr.add_to_screen(bod, msk, pos)
    i = 0
    for obs in obstacle:
        if obs.get_pos()[1] <= 0:
            to_rem_o.append(obs)
            continue
        our_list = obs.body()
        # print(our_list)
        # exit()
        for a_a in our_list:
            f_f1, f_f2, poses = a_a
            # print(f_f1, f_f2, poses)
            scr.add_to_screen(f_f1, f_f2, poses)
        i += 1
        # exit()
    for a_a in to_rem_o:
        obstacle.remove(a_a)
        del a_a
    i = 0
    to_rem_b = []
    for bullet in bullets:
        f_f1, f_f2 = bullet.body()
        if bullet.get_pos()[1] >= SCREENWIDTH-np.shape(f_f1)[1]-1:
            to_rem_b.append(bullet)
            continue
        scr.add_to_screen(f_f1, f_f2, bullet.get_pos())
        i += 1
    for a_a in to_rem_b:
        bullets.remove(a_a)
        del a_a
    scr.add_to_screen(*(boss.body()), boss.get_pos())
    i = 0
    for snowball in snowballs:
        f_f1, f_f2 = snowball.body()
        if snowball.get_pos()[1] <= 0:
            to_rem_s.append(snowball)
            continue
        scr.add_to_screen(f_f1, f_f2, snowball.get_pos())
        i += 1
    for a_a in to_rem_s:
        snowballs.remove(a_a)
        del a_a

    scr.printscreen()


def main():
    global MANUAL_MODE
    global BOSS_MODE
    scr = Screen()
    # lives = 3
    playing = 1
    # coins_collected = 0
    died = 0
    reset()
    while playing == 1:
        if died == 1:
            # if lives != 0:
            #     died = 0
            #     destroy(per)
            #     time.sleep(2)
            #     # create_map()
            # else:
            clear()
            print(Back.WHITE + Fore.BLACK +
                  """┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
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
                    """)
            sys.exit()
        snowballs = []
        boss = Boss()
        per = Mandalorian()
        keypress = KBHit()
        bod, msk = per.body()
        pos = per.return_pos()
        coins = []
        obstacles = []
        bullets = []
        magnets = []
        scr.add_to_screen(bod, msk, pos)
        while True:
            tick()
            if keypress.kbhit():
                c_h = keypress.getch()
                if c_h == 'w':
                    per.move_up(3)
                elif c_h == 's':
                    per.move_down(1)
                elif c_h == 'a':
                    per.move_left(3)
                elif c_h == 'd':
                    per.move_right(3)
                elif c_h == ' ':
                    if len(bullets) < 3:
                        bullets.append(per.shoot())
                elif c_h == '1':
                    new_c = random_coin_gen()
                    coins.extend(new_c)
                elif c_h == '2':
                    new_o = obstacle_gen()
                    obstacles.append(new_o)
                elif c_h == '3':
                    new_m = magnet_spawner()
                    magnets.append(new_m)
                elif c_h == '4':
                    new_s = boss.shoot()
                    snowballs.append(new_s)
                else:
                    died = 1
                    break
            clear()
            scr.clrscr()
            update_objects(per, coins, obstacles, bullets,
                           magnets, boss, snowballs)
            if not (MANUAL_MODE or BOSS_MODE):
                if np.random.random_sample()*(len(coins)+1) < 0.04:
                    new_c = random_coin_gen()
                    coins.extend(new_c)
                if np.random.random_sample()*(len(obstacles)+1) < 0.04:
                    new_o = obstacle_gen()
                    obstacles.append(new_o)
                if np.random.random_sample()*(500*len(magnets)+1) < 0.04:
                    new_m = magnet_spawner()
                    magnets.append(new_m)
            if BOSS_MODE and (not MANUAL_MODE):
                if np.random.random_sample()*len(snowballs) < 0.06:
                    new_s = boss.shoot()
                    snowballs.append(new_s)
            render_objects(scr, bod, msk, per, coins,
                           obstacles, bullets, magnets, boss, snowballs)
            check_collisions(per, obstacles, magnets, coins,
                             bullets, boss, snowballs)
            time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
