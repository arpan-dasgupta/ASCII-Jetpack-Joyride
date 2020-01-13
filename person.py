import numpy as np
from bullet import Bullet


class Person:
    cur_pos = [0, 0]

    def body(self):
        pass

    def shoot(self):
        bullet = Bullet(self.cur_pos.copy())
        return bullet

    def move(self):
        pass
