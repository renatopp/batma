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

'''Resource handlers'''

import pygame
import batma
from batma import gl
from batma.maths import mathematic as math


def load_image(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, 'RGBA', 1)

    width = texture_surface.get_width()
    height = texture_surface.get_height()
    # texture = gl.glGenTextures(1)
    texture = [int(t) for t in gl.glGenTextures(1)] 

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, texture_data)

    return Image(texture, width, height)


def load_text(text, font_size=16, font_name=None, color=None, antialias=True):
    color = color or batma.display.default_color

    font_obj = pygame.font.SysFont(font_name, font_size)
    image = font_obj.render(text, antialias, color.to_pygame())
    height = image.get_height()
    width = image.get_width()

    h = int(2**math.ceil(math.log(height, 2)))
    w = int(2**math.ceil(math.log(width, 2)))

    texture = gl.glGenTextures(1) 
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    
    empty_list = "\x00" * w*h*4
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, w, h, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, empty_list)
    
    texture_data = pygame.image.tostring(image, "RGBA", 1)
    gl.glTexSubImage2D(gl.GL_TEXTURE_2D, 0, 0, 0, image.get_width(), image.get_height(), gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, texture_data)

    image = Image(texture, w, h)
    image.width = width
    image.height = height

    return image


class Image(object):
    def __init__(self, texture, width, height):
        self.texture = texture
        self.width = width
        self.height = height
        self.__display_list = self.__create_display_list(texture, width, height)

    def get_size(self):
        return batma.Vector2(self.width, self.height)
    def set_size(self, value):
        self.width, self.height = value
    size = property(get_size, set_size)
    
    def __create_display_list(self, texture, width, height):
        display_list = gl.glGenLists(1)
        gl.glNewList(display_list, gl.GL_COMPILE);
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
        gl.glBegin(gl.GL_QUADS)
        gl.glTexCoord2f(0, 0); gl.glVertex2f(0, 0)
        gl.glTexCoord2f(0, 1); gl.glVertex2f(0, height)
        gl.glTexCoord2f(1, 1); gl.glVertex2f(width, height)
        gl.glTexCoord2f(1, 0); gl.glVertex2f(width, 0)
        gl.glEnd()
        gl.glEndList()

        return display_list
        
    def draw(self):
        gl.glCallList(self.__display_list)
