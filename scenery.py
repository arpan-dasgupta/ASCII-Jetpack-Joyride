import numpy as np
from colorama import Fore
from moving import Moving
from config import SCREENHEIGHT,SCREENWIDTH


class Scenery(Moving):

    bod = np.array([])
    msk = np.array([])

    def __init__(self):
        sample = np.random.random_sample()
        if sample < 0.3:
            self.bod = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['~'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['*'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['~'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['*'],['-'],['-'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['~'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['*'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],['_'],[' '],[' '],[' '],['_'],['!'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],['*'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],[' '],[' '],[' '],['/'],[' '],[' '],['\\'],['_'],[' '],[' '],['_'],['/'],[' '],['\\'],[' '],[' '],['|'],[':'],[':'],['|'],[' '],['_'],['_'],['_'],[' '],['*'],['*'],['-'],['-'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],['*'],[' '],[' '],[' '],['~'],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['/'],[' '],['\\'],['_'],['/'],['^'],[' '],[' '],[' '],[' '],['\\'],['/'],[' '],[' '],[' '],['^'],['\\'],['/'],['|'],[':'],[':'],['|'],['\\'],['|'],[':'],['|'],[' '],[' '],['*'],['*'],['-'],['-'],['-'],['*'],['*'],['*'],['*'],['*'],['/'],['^'],['\\'],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['\\'],['/'],[' '],[' '],['^'],[' '],['/'],[' '],[' '],['^'],[' '],[' '],[' '],[' '],['/'],[' '],['^'],[' '],['_'],['_'],['_'],['|'],[':'],[':'],['|'],['_'],['|'],[':'],['|'],['_'],['/'],['\\'],['_'],['*'],['*'],['*'],['*'],['*'],['*'],['/'],[' '],[' '],['^'],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],['\\'],[' '],[' '],['_'],['/'],[' '],['^'],[' '],['^'],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['|'],[':'],[':'],['|'],['-'],['-'],['|'],[':'],['|'],['-'],['-'],['-'],['|'],[' '],[' '],['\\'],['_'],['_'],['/'],[' '],[' '],['^'],[' '],[' '],[' '],[' '],[' '],['^'],['\\'],['_'],['_'],['_'],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['_'],['/'],['_'],['^'],[' '],[' '],['\\'],['/'],[' '],[' '],['^'],[' '],[' '],[' '],[' '],['_'],['/'],[' '],['^'],[' '],[' '],[' '],['|'],[':'],[':'],['|'],[':'],[':'],['|'],[':'],['|'],['-'],[':'],[':'],['|'],[' '],['^'],[' '],['/'],['_'],[' '],[' '],['^'],[' '],[' '],[' '],[' '],['^'],[' '],[' '],['^'],[' '],[' '],[' '],['\\'],['_'],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],['\\'],['^'],[' '],['/'],[' '],[' '],[' '],[' '],['/'],['\\'],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],[':'],[':'],['|'],['-'],['-'],['|'],[':'],['|'],[':'],['-'],['-'],['|'],[' '],[' '],['/'],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['^'],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],['\\'],['/'],[' '],[' '],[' '],[' '],['/'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['|'],[':'],[':'],['|'],[':'],[':'],['|'],[':'],['|'],[':'],['-'],[':'],['|'],[' '],['/'],[' '],['^'],[' '],[' '],['\\'],[' '],[' '],['^'],[' '],[' '],[' '],[' '],[' '],[' '],['^'],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],],
                                [[' '],[' '],[' '],['_'],['Q'],[' '],[' '],[' '],['/'],[' '],['_'],['Q'],[' '],[' '],['_'],['Q'],['_'],['Q'],[' '],[' '],['/'],[' '],['_'],['Q'],[' '],[' '],[' '],[' '],['_'],['Q'],[' '],[' '],[' '],['|'],[':'],[':'],['|'],[':'],[':'],['|'],[':'],['|'],[':'],[':'],[':'],['|'],['/'],[' '],[' '],[' '],[' '],['^'],[' '],['\\'],[' '],[' '],[' '],['_'],['Q'],[' '],[' '],[' '],[' '],[' '],[' '],['^'],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],['/'],['_'],['\\'],[')'],[' '],[' '],[' '],['/'],['_'],['\\'],[')'],['/'],['_'],['/'],['\\'],['\\'],[')'],[' '],[' '],['/'],['_'],['\\'],[')'],[' '],[' '],['/'],['_'],['\\'],[')'],[' '],[' '],['|'],[':'],[':'],['|'],[':'],[':'],['|'],[':'],['|'],[':'],[':'],[':'],['|'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['_'],['\\'],[')'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [['_'],['O'],['|'],['/'],['O'],['_'],['_'],['_'],['O'],['|'],['/'],['O'],['_'],['O'],['O'],['|'],['/'],['O'],['_'],['_'],['O'],['|'],['/'],['O'],['_'],['_'],['O'],['|'],['/'],['O'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['O'],['|'],['/'],['O'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],],
                                [['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],['/'],]])
            self.msk = np.full(np.shape(self.bod),Fore.WHITE)
            self._posval = [SCREENHEIGHT - np.shape(self.msk)[0],SCREENWIDTH]
        elif sample < 0.7:
            self.bod = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['*'],['*'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['*'],['*'],['*'],['*'],['\\'],[' '],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],['/'],['*'],['*'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],['/'],['\\'],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['/'],['\\'],['/'],['\\'],['/'],['\\'],[' '],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],['/'],[' '],[' '],['\\'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],['/'],[' '],[' '],['\\'],['/'],['\\'],['/'],[' '],[' '],['\\'],['/'],[' '],[' '],['\\'],[' '],[' '],['/'],['\\'],['/'],[' '],[' '],['\\'],['/'],['\\'],[' '],[' '],['/'],['\\'],[' '],[' '],['/'],['\\'],['/'],[' '],['/'],[' '],['/'],[' '],[' '],['\\'],['/'],[' '],[' '],['\\'],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],['/'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],['/'],[' '],['/'],['\\'],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],[' '],['\\'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],['/'],[' '],['/'],[' '],[' '],[' '],['/'],[' '],[' '],['\\'],['/'],[' '],[' '],['\\'],['/'],[' '],[' '],['\\'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],['\\'],[' '],[' '],],
                                [[' '],[' '],[' '],['/'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],['/'],[' '],[' '],['\\'],['/'],['\\'],[' '],[' '],[' '],['\\'],[' '],[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],['/'],[' '],[' '],[' '],['/'],[' '],[' '],[' '],[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [['_'],['_'],['/'],['_'],['_'],['/'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['/'],['_'],['_'],['_'],['/'],['_'],['_'],['\\'],['_'],['_'],['_'],['\\'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],['_'],]])
            self.msk = np.full(np.shape(self.bod),Fore.WHITE)
            self._posval = [SCREENHEIGHT - np.shape(self.msk)[0],SCREENWIDTH]
        else:
            self.bod = np.array([[[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['.'],['-'],['~'],['~'],['~'],['-'],['.'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],[' '],['.'],['-'],[' '],['~'],[' '],['~'],['-'],['('],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[')'],['_'],[' '],['_'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],],
                                [[' '],['/'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['~'],[' '],['-'],['.'],[' '],[' '],[' '],],
                                [['|'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],[','],],
                                [[' '],['\\'],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['.'],['\''],],
                                [[' '],[' '],[' '],['~'],['-'],[' '],['.'],['_'],[' '],[','],['.'],[' '],[','],['.'],[','],['.'],[','],['.'],[','],[' '],[','],['.'],['.'],[' '],['-'],['~'],[' '],[' '],[' '],],
                                [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],[' '],[' '],[' '],[' '],[' '],[' '],[' '],['\''],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],]])
            self.msk = np.full(np.shape(self.bod),Fore.WHITE)
            self._posval = [0,SCREENWIDTH]

    def body(self):
        return self.bod,self.msk


if __name__ == "__main__":
    s = Scenery()
    ff,_ = s.body()
    for row in ff:
        for col in row:
            for ele in col:
                print(ele,end='')
        print()
