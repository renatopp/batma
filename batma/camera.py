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

import pyglet
from batma.node import BatmaNode
from batma.algebra import Vector2

class Camera(BatmaNode):
    def __init__(self, position=(0, 0), rotation=0.0, scale=1.0, following=None):
        super(Camera, self).__init__()
        self.position = position
        self.rotation = rotation
        self.scale = scale
        
        self.following = following
    
    def look_at(self, x, y):
        self.position = x, y

    def follow(self, obj):
        self.following = obj

    def update(self, tick):
        if self.following:
            self.position = self.following.position
    
    def reset(self, center):
        self.__x = self.x
        self.__y = self.y
        self.__scale = self.scale
        pyglet.gl.glTranslatef(-self.__x*self.__scale+center[0], -self.__y*self.__scale+center[1], 0)
    
        if self.rotation != 0.0:
            pyglet.gl.glTranslatef(self.__x*self.__scale, self.__y*self.__scale, 0)
            pyglet.gl.glRotatef(self.rotation, 0, 0, 1)
            pyglet.gl.glTranslatef(-self.__x*self.__scale, -self.__y*self.__scale, 0)

        if self.scale != 1.0:
            pyglet.gl.glScalef(self.scale, self.scale, 1)
        
    def apply(self, center):
        pyglet.gl.glTranslatef(self.__x*self.__scale+center[0], self.__y*self.__scale+center[1], 0)
        


