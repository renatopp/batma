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

__all__ = ['Camera']

import pygame
import batma
from batma.maths.algebra import Vector2
from batma.core.gameobject import GameObject

class Camera(GameObject):
    '''Represents a 2D camera on the game'''
    
    def __init__(self, position=(0, 0), rotation=0, scale=1, anchor='center'):
        super(Camera, self).__init__(position, rotation, scale, anchor)

        # print  int(batma.display.width*2),  int(batma.display.height*2)
        self.original_surface = pygame.Surface(
            (int(batma.display.width*2), int(batma.display.height*2))
        )
        self.surface = self.original_surface.copy()
        # self.rect = batma.display.rect.copy()
        
        self.set_rotation(rotation)
        self.set_scale(scale)
        self.set_anchor(anchor)

    def _do_rotation(self, cascade=True):
        pass

    def _do_scaling(self, cascade=True):
        pass

    def draw(self):
        pass


    def __repr__(self):
        return '<Camera (%d, %d)>'%(self.rect.center)
    __str__ = __repr__