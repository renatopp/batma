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
from batma import gl
from batma.core.gameobject import GameObject


class Sprite(GameObject):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1, anchor='center'):
        self.color = batma.colors.WHITE
        self.width = 0
        self.height = 0
        self.__anchor_x = 0
        self.__anchor_y = 0
        self.__anchor_name_x = 'center'
        self.__anchor_name_y = 'center'

        super(Sprite, self).__init__()
        self.__image = None
        
        self.set_image(image)
        self.set_position(position)
        self.set_rotation(rotation)
        self.set_scale(scale)
        self.set_anchor(anchor)

    def set_scale(self, value):
        super(Sprite, self).set_scale(value)
        self.width = self.__image.width*self.scale[0]
        self.height = self.__image.height*self.scale[1]        

    def get_image(self):
        return self.__image
    def set_image(self, image):
        if isinstance(image, basestring):
            image = batma.resource.load_image(image)

        self.__image = image
        self.width = self.__image.width*self.scale[0]
        self.height = self.__image.height*self.scale[1]
        self.__update_anchor()
    image = property(get_image, set_image)

    def get_anchor_x(self):
        return self.__anchor_x
    def set_anchor_x(self, value):
        if isinstance(value, basestring):
            self.__anchor_name_x = value
            value = value.lower()
            if value == 'topleft' or value == 'bottomleft':
                self.__anchor_x = 0
            elif value == 'topright' or value == 'bottomright': 
                self.__anchor_x = self.image.width
            else:
                self.__anchor_x = self.image.width/2.0
        else:
            self.__anchor_x = value
            self.__anchor_name_x = 'custom'

        # self.rect.x = self.__x - self.__anchor_x
    anchor_x = property(get_anchor_x, set_anchor_x)

    def get_anchor_y(self):
        return self.__anchor_y
    def set_anchor_y(self, value):
        if isinstance(value, basestring):
            self.__anchor_name_y = value
            value = value.lower()
            if value == 'bottomleft' or value == 'bottomright': 
                self.__anchor_y = 0
            elif value == 'topleft' or value == 'topright':
                self.__anchor_y = self.image.height
            else:
                self.__anchor_y = self.image.height/2.0
        else:
            self.__anchor_y = value
            self.__anchor_name_y = 'custom'
    anchor_y = property(get_anchor_y, set_anchor_y)

    def get_anchor(self):
        return Vector2(self.__anchor_x, self.__anchor_y)
    def set_anchor(self, value):
        if isinstance(value, basestring):
            value = [value, value]
        self.anchor_x = value[0]
        self.anchor_y = value[1]
    anchor = property(get_anchor, set_anchor)

    def add_circle_collider(self, position=None, radius=None):
        if position is None:
            position = self.position

        if radius is None:
            radius = max(self.width, self.height)/2.0

        self.collider = batma.CircleCollider(position, radius)

    def add_box_collider(self, position=None, half_width=None, half_height=None):
        if position is None:
            position = self.position

        if half_width is None:
            half_width = self.width/2.0

        if half_height is None:
            half_height = self.height/2.0

        self.collider = batma.BoxCollider(position, half_width, half_height)

    def __update_anchor(self):
        if self.__anchor_name_x == 'custom':
            self.set_anchor_x(self.__anchor_x)
        else:
            self.set_anchor_x(self.__anchor_name_x)

        if self.__anchor_name_y == 'custom':
            self.set_anchor_y(self.__anchor_y)
        else:
            self.set_anchor_y(self.__anchor_name_y)

    def draw(self):
        if self.visible:
            gl.glPushMatrix()
            gl.glColor4fv(self.color)

            self.transform()
            gl.glTranslatef(-self.anchor_x, -self.anchor_y, 0)
            
            self.image.draw()
            # gl.glCallList(self.image.display_list)
            gl.glPopMatrix()