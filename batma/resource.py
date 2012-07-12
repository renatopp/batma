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
from batma.maths import mathematic as math
from OpenGL import GL as gl
from OpenGL import GLU as glu

def _create_display_list(texture, width, height):
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

def load_image_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, 'RGBA', 1)

    width = texture_surface.get_width()
    height = texture_surface.get_height()
    texture = gl.glGenTextures(1)

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, texture_data)

    return texture, width, height

def load_text_texture(text, font_size=48, font_name=None, color=None, antialias=True):
    color = color or batma.display.default_color

    font_obj = pygame.font.Font(font_name, font_size)
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

    return texture, width, height, w, h

def load_image(filename):
    return Image(*load_image_texture(filename))

def load_text(text, font_size=48, font_name=None, color=None, antialias=True):
    color = color or batma.display.default_color

    texture, width, height, w, h = load_text_texture(text, font_size, font_name, color, antialias)
    image = Image(texture, w, h)
    image.width = width
    image.height = height

    return image

class Image(object):
    def __init__(self, texture, width, height):
        self.texture = texture
        self.width = width
        self.height = height
        self.display_list = _create_display_list(self.texture, self.width, self.height)

    def draw(self, position=(0, 0), rotation=0.0, scale=(1.0, 1.0), anchor=None, 
                  color=None):
        color = color or batma.colors.WHITE

        gl.glPushMatrix()

        gl.glColor4fv(color)

        if anchor is None:
            anchor = self.width/2, self.height/2

        gl.glTranslatef(position[0]-anchor[0], position[1]-anchor[1], 0)
        gl.glTranslate(anchor[0], anchor[1], 0)

        if rotation != 0.0:
            gl.glRotatef(rotation, 0, 0, -1)

        if scale != (1.0, 1.0):
            gl.glScalef(scale[0], scale[1], 0)

        gl.glTranslate(-anchor[0], -anchor[1], 0)

        gl.glCallList(self.display_list)
        gl.glPopMatrix()