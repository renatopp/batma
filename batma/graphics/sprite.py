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

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1, anchor='center'):
        super(Sprite, self).__init__()

        self.image = pygame.surface.Surface((0, 0))
        self.original_image = self.image
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.__anchor = batma.Vector2(0, 0)
        self.__untransformed_nor_anchor = batma.Vector2(0, 0)

        self.__position = None
        self.__scale = None
        self.__rotation = None

        self.__is_scale_pending = False
        self.__is_rotation_pending = False

        if isinstance(image, basestring):
            image = pygame.image.load(image).convert_alpha()

        self.set_position(position)
        self.set_scale(scale)
        self.set_rotation(rotation)
        self.apply_texture(image)

    def apply_texture(self, image):
        self.image = image
        self.original_image = image.copy()
        self.anchor = batma.Vector2(image.get_width()/2.0, image.get_height()/2.0)
        self.rect.x = self.position[0]-self.anchor[0]
        self.rect.y = self.position[1]-self.anchor[1]
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()

        self.__is_scale_pending = True
        self.__is_rotation_pending = True

    def get_anchor(self):
        return self.__anchor
    def set_anchor(self, value):
        self.__anchor = value
        self.__untransformed_nor_anchor = batma.Vector2(
            self.__anchor[0]/self.original_image.get_width(),
            self.__anchor[1]/self.original_image.get_height()
        )
        self.__update_rect()
    anchor = property(get_anchor, set_anchor)

    def get_x(self):
        return self.__position.x
    def set_x(self, value):
        self.__position.x = value
        self.__update_rect()
    x = property(get_x, set_x)

    def get_y(self):
        return self.__position.y
    def set_y(self, value):
        self.__position.y = value
        self.__update_rect()
    y = property(get_y, set_y)

    def get_position(self):
        # return batma.Vector2(self.rect.centerx, self.rect.centery)
        return self.__position
    def set_position(self, value):
        self.__position = batma.Vector2(value[0], value[1])
        self.__update_rect()
    position = property(get_position, set_position)

    def get_rotation(self):
        return self.__rotation
    def set_rotation(self, value):
        self.__rotation = value%360
        self.__is_rotation_pending = True
    rotation = property(get_rotation, set_rotation)

    def get_scale(self):
        return self.__scale
    def set_scale(self, value):
        if isinstance(value, (int, long, float)):
            value = batma.Vector2(value, value)
        self.__scale = value
        self.__is_scale_pending = True
    scale = property(get_scale, set_scale)

    def __update_rect(self):
        self.rect.x = self.position[0] - self.anchor[0]
        self.rect.y = self.position[1] - self.anchor[1]

    def __resize_surface_extents(self):
        """Handles surface cleanup once a scale or rotation operation has been performed."""
        self.anchor[0] = self.image.get_width() * self.__untransformed_nor_anchor[0]
        self.anchor[1] = self.image.get_height() * self.__untransformed_nor_anchor[1]
        self.__update_rect()
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()

    def __execute_scale(self, image):
        """Execute the scaling operation"""
        size_to_scale_from = image.get_size()
        x = size_to_scale_from[0] * self.__scale[0]
        y = size_to_scale_from[1] * self.__scale[1]
        scaled_value = (int(x), int(y))
        self.image = pygame.transform.scale(image, scaled_value)
        self.__resize_surface_extents()

    def __execute_rotation(self):
        """Executes the rotating operation"""
        self.image = pygame.transform.rotate(self.original_image, -self.__rotation)
        self.__resize_surface_extents()

    def __handle_scale_rotation(self):
        if self.__is_rotation_pending == True:
            self.__execute_rotation()
            self.__is_rotation_pending = False

            #Scale the image using the recently rotated surface to keep the orientation correct
            if self.scale != (1, 1):
                self.__execute_scale(self.image)
                self.__is_scale_pending = False

        #The image is not rotating while scaling, thus use the untransformed image to scale.
        if self.__is_scale_pending == True:
            image = self.original_image

            if self.rotation != 0:
                self.__execute_rotation()
                self.__is_rotation_pending = False
                image = self.image

            self.__execute_scale(image)
            self.__is_scale_pending = False

    def draw(self):
        self.__handle_scale_rotation()
        batma.display.screen.blit(self.image, self.rect)


