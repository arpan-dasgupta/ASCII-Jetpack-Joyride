from colorama import Fore
import numpy as np
from person import Person
import config


class Dragon(Person):

    cur_pos = [0, 0]
    stages = []
    ud_stages = []
    mask = np.array([])
    alt_mask = np.array([])
    call_count=0
    countdir = 1
    last_vals = [0,0,0,0,0]

    def body(self):
        avg = 0
        for val in self.last_vals:
            avg+=val
        if avg>1:
            return self.ud_stages[0],self.alt_mask
        elif avg<-1:
            return self.ud_stages[1],self.mask

        if self.call_count == 0:
            self.countdir = 1
        if self.call_count == 4:
            self.countdir = -1
        self.call_count += self.countdir
        return self.stages[self.call_count],self.mask

    def get_pos(self):
        return self.cur_pos

    def __init__(self):
        self.cur_pos = [0,0]
        a = np.array([[['_'], ['_'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['_'], ['_'], [' '], ['|'], ['\\'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ],
                      [[' '], [' '], ['-'], ['-'], ['_'], ['_'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['_'],
                       ['_'], ['-'], ['-'], [' '], [' '], ['~'], [' '], [' '], ['^'], ['^'], ['^'], ['\\'], ['\\'], [' '], [' '], ],
                      [['_'], ['_'], [' '], [' '], [' '], [' '], ['-'], ['-'], ['_'], ['_'], ['_'], ['_'], ['-'], ['-'], [' '],
                       [' '], [' '], [' '], ['_'], ['_'], [' '], [' '], [' '], [' '], [' '], ['\''], ['`'], ['~'], ['~'], ['P'], ],
                      [[' '], [' '], ['-'], ['-'], ['_'], ['_'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['_'],
                       ['_'], ['-'], ['-'], [' '], [' '], ['\\'], ['\\'], ['\\'], ['_'], [' '], [';'], ['-'], ['-'], ['^'], ['^'], ],
                      [[' '], [' '], [' '], [' '], [' '], [' '], ['-'], ['-'], ['_'], ['_'], ['_'], ['_'], ['-'], ['-'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['\\'], ['_'], ['\\'], [' '], ['~'], ['.'], ]])
        self.stages.append(a)
        a = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],[' '],[' '],['-'],['-'],['_'],['_'],['-'],['~'],[' '],[' '],['^'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [[' '],[' '],['-'],['-'],['_'],['_'],['_'],['-'],['-'],[' '],[' '],[' '],[' '],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],[' '],[' '],['-'],['-'],['_'],['_'],['-'],['\\'],['\\'],['\\'],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [[' '],[' '],['-'],['-'],['_'],['_'],['_'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],]])
        self.stages.append(a)
        a = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],['_'],['_'],[' '],[' '],['_'],['_'],['-'],['-'],['~'],[' '],[' '],['^'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [['-'],['-'],['_'],['_'],['_'],['_'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],['_'],['_'],[' '],[' '],['_'],['_'],['-'],['-'],['\\'],['\\'],['\\'],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [['-'],['-'],['_'],['_'],['_'],['_'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],]])
        self.stages.append(a)
        a = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [['-'],['-'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['-'],['-'],[' '],[' '],['-'],['-'],['_'],['_'],['~'],[' '],[' '],['^'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [['-'],['-'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['-'],['-'],[' '],[' '],['-'],['-'],['_'],['_'],['\\'],['\\'],['\\'],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],]])
        self.stages.append(a)
        a = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['-'],['-'],['~'],[' '],[' '],['^'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['-'],['-'],['\\'],['\\'],['\\'],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],]])
        self.stages.append(a)
        a=np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['_'],['_'],['~'],[' '],[' '],['^'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [['_'],['_'],['_'],['_'],['_'],['-'],['-'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['-'],['-'],['\\'],['\\'],['\\'],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],['_'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],],
                    [['_'],['_'],['_'],['_'],['_'],['-'],['-'],['-'],['-'],['-'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],]])
        self.ud_stages.append(a)
        a=np.array([[['-'],['-'],['-'],['-'],['-'],['-'],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],['|'],[' '],['\\'],['^'],['^'],['\\'],['\\'],[' '],[' '],],
                    [['-'],['-'],['-'],['-'],['-'],['-'],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['~'],[' '],[' '],['^'],[' '],['\''],['`'],['~'],['~'],['P'],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],[' '],[';'],['-'],['-'],['^'],['^'],],
                    [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['-'],['-'],['-'],['_'],['_'],['\\'],['\\'],['\\'],[' '],['\\'],['_'],['\\'],[' '],['~'],['.'],]])
        self.ud_stages.append(a)

        self.mask = np.full(np.shape(self.stages[0]),Fore.BLACK)
        self.alt_mask = np.full(np.shape(self.ud_stages[0]),Fore.BLACK)

    def move_up(self, val):
        initial = self.cur_pos[0]
        self.cur_pos[0] = max(0, self.cur_pos[0]-val)
        initial -= self.cur_pos[0]
        self.last_vals.pop(0)
        self.last_vals.append(initial)

    def move_down(self, val):
        initial = self.cur_pos[0]
        self.cur_pos[0] = min(config.SCREENHEIGHT-np.shape(self.stages[0])[0]-2, self.cur_pos[0]+val)
        initial -= self.cur_pos[0]
        self.last_vals.pop(0)
        self.last_vals.append(initial)
    



if __name__ == "__main__":
    fd = open('temp', 'r')
    a = fd.read()
    # print(a)
    print('[[', end='')
    for x in a:
        if x == "\n":
            print('],'+x+'[', end='')
        else:
            if x == '\'' or x == '\"' or x == '\\':
                print('[\''+'\\'+x+'\'],', end='')
            else:
                print('[\''+x+'\'],', end='')
    print(']]')
    x = 3 if True else 2
