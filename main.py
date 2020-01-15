import sys
import time
from colorama import Fore, Back
import numpy as np
from background import Screen
from boss import Boss
from coins import random_coin_gen
from collision import collision_checker
from config import clear, tick, SLEEP_TIME, reset, clear_2
from dragon import Dragon
from hor_obstacles import obstacle_gen
from kbhit import KBHit
from magnet import Magnet, magnet_spawner
from player import Mandalorian, SCREENWIDTH
from scenery import Scenery
from snowball import Snowball
import config


def check_collisions(per, obstacles, magnets, coins, bullets, boss, snowballs, dragon):
    if config.DRAGON_MODE:
        per = dragon
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
    for snowball in snowballs:
        part3, _ = per.body()
        part1, _ = snowball.body()
        if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                np.shape(part3)[0], np.shape(part3)[1]], snowball.get_pos(), per.return_pos()):
            if not config.DRAGON_MODE and per.shield_status()[0] == 1:
                per.shield_deactivate()
                continue
            return -1
    part3, _ = per.body()
    part1, _ = boss.body()
    if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
            np.shape(part3)[0], np.shape(part3)[1]], boss.get_pos(), per.return_pos()):
        if not config.DRAGON_MODE and per.shield_status()[0] == 1:
            per.shield_deactivate()
        else:
            return -1
    to_rem_b = []
    for bullet in bullets:
        part3, _ = bullet.body()
        part1, _ = boss.body()
        if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                np.shape(part3)[0], np.shape(part3)[1]], boss.get_pos(), bullet.get_pos()):
            boss.get_hit()
            to_rem_b.append(bullet)
            if boss.get_lives() == 0:
                return 2
    for bull in to_rem_b:
        bullets.remove(bull)

    for obstacle in obstacles:
        obs = obstacle.body()
        part3, _ = per.body()
        for indiv in obs:
            part1, _, pos = indiv
            if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                    np.shape(part3)[0], np.shape(part3)[1]], pos, per.return_pos()):
                if not config.DRAGON_MODE and per.shield_status()[0] == 1:
                    per.shield_deactivate()
                    continue
                return -1
    to_rem_c = []
    part3, _ = per.body()
    for coin in coins:
        if collision_checker([np.shape(part3)[0], np.shape(part3)[1]], [1, 1],  per.return_pos(), coin.get_pos()):
            to_rem_c.append(coin)
            config.SCORE += coin.get_val()
    for coin in to_rem_c:
        coins.remove(coin)
    to_rem_s = set()
    to_rem_b = set()
    for snowball in snowballs:
        for bullet in bullets:
            part3, _ = bullet.body()
            part1, _ = snowball.body()
            if collision_checker([np.shape(part1)[0], np.shape(part1)[1]], [
                    np.shape(part3)[0], np.shape(part3)[1]], snowball.get_pos(), bullet.get_pos()):
                to_rem_b.add(bullet)
                to_rem_s.add(snowball)
    for snow in to_rem_s:
        snowballs.remove(snow)
    for bull in to_rem_b:
        bullets.remove(bull)
    return 1


def update_objects(per, coins, obstacles, bullets, magnets, boss, snowballs, dragon, scenes):
    if not config.DRAGON_MODE:
        per.update_pos()
    else:
        dragon.move_up(1)
    if config.DRAGON_MODE:
        per = dragon
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
    for scene in scenes:
        scene.update_pos()
    boss.update_pos(per.return_pos())


def render_objects(scr,  per, coins, obstacle, bullets, magnets, boss, snowballs, dragon, scenes):
    to_rem_c = []
    to_rem_o = []
    to_rem_m = []
    to_rem_s = []
    to_rem_sc = []
    i = 0
    for scene in scenes:
        f_f1, f_f2 = scene.body()
        if scene.get_pos()[1] + np.shape(f_f1)[1] <= 0:
            to_rem_sc.append(scene)
            continue
        scr.add_to_screen(f_f1, f_f2, scene.get_pos(), 1)
        i += 1
    for a_a in to_rem_sc:
        scenes.remove(a_a)
        del a_a
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
    if not config.DRAGON_MODE:
        scr.add_to_screen(*(per.body()), per.return_pos())
    else:
        scr.add_to_screen(*(dragon.body()), dragon.get_pos())
    i = 0
    for obs in obstacle:
        if obs.get_pos()[1] <= 0:
            to_rem_o.append(obs)
            continue
        our_list = obs.body()
        for a_a in our_list:
            f_f1, f_f2, poses = a_a
            scr.add_to_screen(f_f1, f_f2, poses)
        i += 1
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
    scr.printscreen(per.shield_status(), boss.get_lives())


def main():
    scr = Screen()
    config.LIVES = 3
    died = 0
    reset()
    while config.LIVES > 0:
        if died == 1:
            clear()
            died = 0
            time.sleep(2)
        snowballs = []
        boss = Boss()
        per = Mandalorian()
        dragon = Dragon()
        keypress = KBHit()
        pos = per.return_pos()
        coins = []
        scenes = []
        obstacles = []
        bullets = []
        magnets = []
        scr.add_to_screen(*(per.body()), pos)
        while True:
            tick()
            if keypress.kbhit():
                c_h = keypress.getch()
                if c_h == 'w':
                    if config.DRAGON_MODE:
                        dragon.move_up(3)
                    else:
                        per.move_up(2)
                elif c_h == 's':
                    if config.DRAGON_MODE:
                        dragon.move_down(3)
                    else:
                        per.move_down(1)
                elif c_h == 'a':
                    if not config.DRAGON_MODE:
                        per.move_left(3)
                elif c_h == 'd':
                    if not config.DRAGON_MODE:
                        per.move_right(3)
                elif c_h == 'f':
                    if len(bullets) < 3 or config.DRAGON_MODE:
                        if not config.DRAGON_MODE:
                            bullets.append(per.shoot())
                        else:
                            bullets.append(dragon.shoot())
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
                elif c_h == '5':
                    new_s = Scenery()
                    scenes.append(new_s)
                elif c_h == 'y':
                    config.DRAGON_MODE = 1 - config.DRAGON_MODE
                elif c_h == ' ':
                    if not config.DRAGON_MODE:
                        per.shield_activate()
                elif c_h == 'g':
                    if not config.DRAGON_MODE:
                        per.speed_up()
                elif c_h == 'q':
                    died = 1
                    config.LIVES = 0
                    break
            clear()
            scr.clrscr()
            update_objects(per, coins, obstacles, bullets,
                           magnets, boss, snowballs, dragon, scenes)
            if not (config.MANUAL_MODE or config.BOSS_MODE):
                if np.random.random_sample()*(len(coins)+1) < 0.04:
                    new_c = random_coin_gen()
                    coins.extend(new_c)
                if np.random.random_sample()*(len(obstacles)+1) < 0.04:
                    new_o = obstacle_gen()
                    obstacles.append(new_o)
                if np.random.random_sample()*(500*len(magnets)+1) < 0.04:
                    new_m = magnet_spawner()
                    magnets.append(new_m)
                if np.random.random_sample()*(len(scenes) <= 1) < 0.96:
                    new_s = Scenery()
                    scenes.append(new_s)
            if config.BOSS_MODE and (not config.MANUAL_MODE):
                if np.random.random_sample()*len(snowballs) < 0.06:
                    new_s = boss.shoot()
                    snowballs.append(new_s)
            render_objects(scr, per, coins,
                           obstacles, bullets, magnets, boss, snowballs, dragon, scenes)
            stat = check_collisions(per, obstacles, magnets, coins,
                                    bullets, boss, snowballs, dragon)
            if stat == -1:
                died = 1
                config.LIVES -= 1
                break
            if stat == 2:
                clear_2
                print("YOU WIN!")
                exit()
            time.sleep(SLEEP_TIME)
    clear_2()
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
    print("YOUR SCORE - " + str(config.SCORE))


if __name__ == '__main__':
    main()
