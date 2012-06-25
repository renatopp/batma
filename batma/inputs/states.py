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

@singleton
class KeyboardState(object):
    def __init__(self):
        self.state = ()
        self.previous_state = ()

    def update(self):
        self.previous_state = self.state
        self.state = pygame.key.get_pressed()
    
    def __getitem__(self, key):
        return self.state[key]
    
    def is_any_down(self):
        return any(self.state)

    def is_any_clicked(self):
        return any(self.state[i] and not self.previous_state[i] for i in xrange(len(self.previous_state)))

    def is_down(self, key):
        return self.state[key]

    def is_up(self, key):
        return not self.state[key]

    def is_clicked(self, key):
        return self.state[key] and not self.previous_state[key]

@singleton
class MouseState(object):
    def __init__(self):
        self.previous_state = ()
        self.state = ()
        self.x = 0.0
        self.y = 0.0

    def get_position(self):
        return Vector2(self.x, self.y)
    position = property(get_position)

    def update(self):
        self.previous_state = self.state
        self.state = pygame.mouse.get_pressed()
        self.x, self.y = pygame.mouse.get_pos()

    def __getitem__(self, button):
        return self.state[button]
    
    def is_any_down(self):
        return any(self.state)

    def is_any_clicked(self):
        return any(self.state[i] and not self.previous_state[i] for i in xrange(len(self.previous_state)))

    def is_down(self, button):
        return self.state[button]

    def is_up(self, button):
        return not self.state[button]
    
    def is_clicked(self, key):
        return self.state[key] and not self.previous_state[key]
