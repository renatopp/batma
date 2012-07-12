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

__all__ = ['Sprite']

import pygame
import batma
from batma.core.gameobject import GameObject
from OpenGL import GL as gl
from OpenGL import GLU as glu


class Sprite(GameObject):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1, anchor='center'):
        super(Sprite, self).__init__()
        self.image = None
        self.apply_texture(image)
        
        self.set_position(position)
        self.set_rotation(rotation)
        self.set_scale(scale)
        self.set_anchor(anchor)

    def apply_texture(self, image):
        if isinstance(image, basestring):
            image = batma.resource.load_image(image)

        self.image = image
        self.rect.width = image.width
        self.rect.height = image.height
        self.reapply_anchor()

    def draw(self):
        if self.visible:
            gl.glPushMatrix()
            gl.glColor4fv(self.color)
            self.transform()
            gl.glCallList(self.image.display_list)
            gl.glPopMatrix()