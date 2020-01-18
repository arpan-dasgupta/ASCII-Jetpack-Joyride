import numpy as np
from bullet import Bullet


class Person:
    _cur_pos = [0, 0]

    def body(self):
        pass

    def shoot(self):
        bullet = Bullet(self._cur_pos.copy())
        return bullet

    def move(self):
        pass
