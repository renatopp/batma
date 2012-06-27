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


class Sprite(GameObject):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1, anchor='center'):
        self.image = None
        self.original_image = None

        super(Sprite, self).__init__(position, rotation, scale, anchor)

        self.apply_texture(image)
        self.set_rotation(rotation)
        self.set_scale(scale)
        self.set_anchor(anchor)

    def apply_texture(self, image):
        if isinstance(image, basestring):
            image = pygame.image.load(image).convert_alpha()

        self.image = image
        self.original_image = image.copy()
        
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
        self.reapply_anchor()

    def _do_rotation(self, cascade=True):
        if self.original_image is None: return

        self.image = pygame.transform.rotate(self.original_image, -self.rotation)

        if cascade and self.scale != (1, 1):
            self._do_scaling()
        else:
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()
            self.reapply_anchor()

    def _do_scaling(self, cascade=True):
        if self.original_image is None: return

        if cascade and self.rotation != 0.0:
            self._do_rotation(cascade=False)
            image = self.image
        else:
            image = self.original_image

        image_size = image.get_size()
        x = image_size[0] * self.scale[0]
        y = image_size[1] * self.scale[1]
        scaled_value = (int(x), int(y))
        self.image = pygame.transform.scale(image, scaled_value)
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()
        self.reapply_anchor()

    def draw(self):
        super(Sprite, self).draw(self.image)
