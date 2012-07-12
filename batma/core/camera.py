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
from OpenGL import GL as gl
from OpenGL import GLU as glu

class Camera(object):
    '''Represents a 2D camera on the game'''
    
    def __init__(self):
        self.__center_x = 0
        self.__center_y = 0
        self.__eye_x = 0
        self.__eye_y = 0
        self.__eye_z = 0
        self.__up_vector_x = 0
        self.__up_vector_y = 0
        self.__up_vector_z = 0

        self.reset()

    def get_center(self):
        return batma.Vector2(self.__center_x, self.__center_y)
    def set_center(self, value):
        self.__center_x, self.__center_y = value
    center = property(get_center, set_center)

    def get_eye(self):
        return batma.Vector3(self.__eye_x, self.__eye_y, self.__eye_z)
    def set_eye(self, value):
        self.__eye_x, self.__eye_y, self.__eye_z = value
    eye = property(get_eye, set_eye)

    def get_up_vector(self):
        return batma.Vector3(self.__up_vector_x, self.__up_vector_y, self.__up_vector_z)
    def set_up_vector(self, value):
        self.__up_vector_x, self.__up_vector_y, self.__up_vector_z = value
    up_vector = property(get_up_vector, set_up_vector)    

    def reset(self):
        width, height = batma.display.size
        self.eye = (width/2.0, height/2.0, height/1.1566)
        self.center = (width/2.0, height/2.0)
        self.up_vector = (0, 1, 0)

    def look_at(self, position):
        self.center = position
        self.eye = position[0], position[1], self.__eye_z

    def locate(self):
        gl.glLoadIdentity()
        glu.gluLookAt(
            self.__eye_x, self.__eye_y, self.__eye_z,
            self.__center_x, self.__center_y, 0,
            self.__up_vector_x, self.__up_vector_y, self.__up_vector_z
        )

    def __repr__(self):
        return '<Camera (%d, %d)>'%(self.position)
    __str__ = __repr__