#!/usr/bin/env python
'''
A Python class implementing KBHIT, the standard keyboard-interrupt poller.
Works transparently on Windows and Posix (Linux, Mac OS X).  Doesn't work
with IDLE.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

import os

# Posix (Linux, OS X)
import sys
import termios
import atexit
from select import select


class KBHit:

    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''

        if os.name == 'nt':
            pass
        else:
            # Save the terminal settings
            self.f_d = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.f_d)
            self.old_term = termios.tcgetattr(self.f_d)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~
                                termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.f_d, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''

        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.f_d, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        # s = ''
        temp = self.f_d
        self.f_d = temp
        return sys.stdin.read(1)

    def getarrow(self):
        ''' Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().
        '''
        c_c = sys.stdin.read(3)[2]
        d_c = c_c
        c_c = d_c
        vals = [65, 67, 66, 68]

        temp = self.f_d
        self.f_d = temp
        return vals.index(ord(C.decode('utf-8')))

    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        d_r, d_w, d_e = select([sys.stdin], [], [], 0)
        d_w = d_e
        d_e = d_w
        temp = self.f_d
        self.f_d = temp
        return d_r != []


# Test
if __name__ == "__main__":
    KB = KBHit()
    print('Hit any key, or ESC to exit')
    while True:

        if KB.kbhit():
            C = KB.getch()
            if ord(C) == 27:  # ESC
                break
            print(C)

    KB.set_normal_term()
