import config


class Moving:

    _posval = [0, 0]
    __speed_control = 2

    def __init__(self, initpos):
        self._posval = initpos

    def update_pos(self):
        # print(self._posval)
        self._posval[1] -= self.__speed_control + 2 * (config.SPEED_UP == 1)

    def get_pos(self):
        return self._posval
