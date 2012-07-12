# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

__all__ = ['KeyboardState', 'MouseState']

import pygame
import batma
from batma.maths.algebra import Vector2
from batma.util import singleton

class InputState(object):
    def __init__(self):
        self.state = ()
        self.previous_state = ()
        self.map = {}

    def update(self):
        pass

    def __get(self, key, state):
        if isinstance(key, basestring):
            if key not in self.map:
                raise KeyError('Invalid Map Indice: "%s".'%key)

            keys = self.map[key]
            for k in keys:
                if isinstance(k, (tuple, list)):
                    if all(state[i] for i in k):
                        return True
                else:
                    if state[k]: return True

            return False
        else:
            return state[key]

    def __getitem__(self, key):
        return self.__get(key, self.state)

    def is_any_down(self):
        return any(self.state)

    def is_any_clicked(self):
        return any(self.state[i] and not self.previous_state[i] for i in xrange(len(self.previous_state)))

    def is_down(self, key):
        return self.__get(key, self.state)

    def is_up(self, key):
        return not self.__get(key, self.state)

    def is_clicked(self, key):
        return self.__get(key, self.state) and not self.__get(key, self.previous_state)



@singleton
class KeyboardState(InputState):
    def __init__(self):
        InputState.__init__(self)
        self.map = {
            'up': [batma.keys.UP, batma.keys.W],
            'down': [batma.keys.DOWN, batma.keys.S],
            'left': [batma.keys.LEFT, batma.keys.A],
            'right': [batma.keys.RIGHT, batma.keys.D],
            'jump': [batma.keys.SPACE],
            'quit': [batma.keys.ESCAPE, (batma.keys.LALT, batma.keys.F4)]
        }

    def update(self):
        self.previous_state = self.state
        self.state = pygame.key.get_pressed()

@singleton
class MouseState(InputState):
    def __init__(self):
        InputState.__init__(self)
        self.x = 0.0
        self.y = 0.0
        self.map = {
            'left': [batma.buttons.LEFT],
            'middle': [batma.buttons.MIDDLE],
            'right': [batma.buttons.RIGHT],
        }

    def get_position(self):
        return Vector2(self.x, self.y)
    position = property(get_position)

    def update(self):
        self.previous_state = self.state
        self.state = pygame.mouse.get_pressed()
        self.x, self.y = pygame.mouse.get_pos()
        self.y = batma.display.height-self.y