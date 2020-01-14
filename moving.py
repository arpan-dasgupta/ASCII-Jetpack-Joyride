import config


class Moving:

    posval = [0, 0]

    def __init__(self, initpos):
        self.posval = initpos

    def update_pos(self):
        self.posval[1] -= 2 + 2 * (config.SPEED_UP == 1)

    def get_pos(self):
        return self.posval
