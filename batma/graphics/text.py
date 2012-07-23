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

__all__ = ['Text']

import pygame
import batma
from batma.graphics.sprite import Sprite

class Text(Sprite):
    def __init__(self, text, position=(0, 0), rotation=0.0, scale=1.0, 
                       anchor='center', color=None, font_name=None, 
                       font_size=48, antialias=True):
        
        image = batma.resource.load_text(text, font_size, font_name, color, antialias)
        super(Text, self).__init__(image, position, rotation, scale, anchor)

        self.__text = text
        self.__color = color or batma.display.default_color
        self.__font_name = font_name
        self.__font_size = font_size
        self.__antialias = antialias
        self.__pending_render = False
        self.static = True

        self.collider = None
    def get_text(self):
        return self.__text
    def set_text(self, value):
        self.__text = value
        self.__pending_render = True
    text = property(get_text, set_text)

    def get_color(self):
        return self.__color
    def set_color(self, value):
        self.__color = value
        self.__pending_render = True
    color = property(get_color, set_color)

    def get_font_name(self):
        return self.__font_name
    def set_font_name(self, value):
        self.__font_name = value
        self.__pending_render = True
    font_name = property(get_font_name, set_font_name)

    def get_font_size(self):
        return self.__font_size
    def set_font_size(self, value):
        self.__font_size = value
        self.__pending_render = True
    font_size = property(get_font_size, set_font_size)

    def get_antialias(self):
        return self.__antialias
    def set_antialias(self, value):
        self.__antialias = value
        self.__pending_render = True
    antialias = property(get_antialias, set_antialias)

    def __render(self):
        self.image = batma.resource.load_text(
            text=self.text, 
            font_size=self.font_size, 
            font_name=self.font_name, 
            color=self.color, 
            antialias=self.antialias
        )

    def draw(self):
        if self.__pending_render:
            self.__render()

        super(Text, self).draw()