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

__all__ = ['Display']

import pygame
import batma
from batma.maths.algebra import Vector2
from batma.util import singleton
from OpenGL import GL as gl
from OpenGL import GLU as glu

@singleton
class Display(object):
    '''
    Class to handle and store all informations and functions relative to screen
    and the game window.
    '''
    def __init__(self, caption=u'Batma Game', size=(640, 480), resizable=False, 
                       fullscreen=False, max_fps=60):
        self.__caption = caption
        self.__width, self.__height = size
        self.__resizable = resizable
        self.__fullscreen = fullscreen
        self.__screen = None
        self.__show_cursor = True

        self.background_color = batma.colors.LAVANDER_BLUE
        self.default_color = batma.colors.BLACK
        self.max_fps = max_fps
        self.show_fps = False

        self.set_caption(caption)

    def get_screen(self):
        return self.__screen
    screen = property(get_screen)

    def get_rect(self):
        return self.__screen.get_rect()
    rect = property(get_rect)

    def get_center(self):
        return Vector2(self.__width/2, self.__height/2)
    center = property(get_center)

    def get_show_cursor(self):
        return self.__show_cursor
    def set_show_cursor(self, value):
        self.__show_cursor = value
        pygame.mouse.set_visible(value)
    show_cursor = property(get_show_cursor, set_show_cursor)

    def get_fullscreen(self):
        return self.__fullscreen
    def set_fullscreen(self, value):
        self.__fullscreen = value
        self.__update_mode()
    fullscreen = property(get_fullscreen, set_fullscreen)

    def get_resizable(self):
        return self.__resizable
    def set_resizable(self, value):
        self.__resizable = value
        self.__update_mode()
    resizable = property(get_resizable, set_resizable)

    def get_width(self):
        return self.__width
    def set_width(self, value):
        self.__width = value
        self.__update_mode()
    width = property(get_width, set_width)

    def get_height(self):
        return self.__height
    def set_height(self, value):
        self.__height = value
        self.__update_mode()
    height = property(get_height, set_height)

    def get_size(self):
        return Vector2(self.__width, self.__height)
    def set_size(self, value):
        self.__width, self.__height = value
        self.__update_mode()
    size = property(get_size, set_size)

    def get_caption(self):
        return self.__caption
    def set_caption(self, value):
        self.__caption = value
        pygame.display.set_caption(value)
    caption = property(get_caption, set_caption)

    def __update_mode(self):
        self.set_caption(self.caption)

        flags = pygame.OPENGL|pygame.HWSURFACE|pygame.DOUBLEBUF
        if self.resizable:
            flags = flags|pygame.RESIZABLE
        if self.fullscreen:
            flags = flags|pygame.FULLSCREEN

        self.__screen = pygame.display.set_mode((self.width, self.height), flags)

        self.clear()
        
        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST)

        self.__set_projection()
        self.__set_depth()
        self.__set_blending()


    def __set_projection(self):        
        gl.glViewport(0, 0, self.width, self.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(60, self.width/float(self.height), 0.1, 3000.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def __set_depth(self, value=True):
        if value:
            gl.glClearDepth(1.0)
            gl.glEnable(gl.GL_DEPTH_TEST)
            gl.glDepthFunc(gl.GL_LEQUAL)
            gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)
        else:
            gl.glDisable(gl.GL_DEPTH_TEST)

    def __set_blending(self):
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    def init(self):
        self.__update_mode()
        
    def clear(self, color=None):
        gl.glClearColor(*self.background_color)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    def apply_config(self, caption=None, size=None, resizable=None, fullscreen=None, max_fps=None):
        self.__caption = caption or self.__caption
        self.__width, self.__height = size or self.size
        self.__fullscreen = fullscreen or self.__fullscreen
        self.__resizable = resizable or self.__resizable
        self.max_fps = max_fps or self.max_fps

        self.__update_mode()
        self.set_caption(self.__caption)

    def draw(self, obj, rect):
        self.screen.blit(obj, rect)