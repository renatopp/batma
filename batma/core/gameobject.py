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

__all__ = ['GameObject']

import pygame
import batma
import weakref
from batma import gl
from batma.util import WeakList
from batma.maths.algebra import Vector2

class GameObject(object):
    __ID = 1

    @classmethod
    def __new_id(cls):
        id = cls.__ID
        cls.__ID += 1
        return id

    def __init__(self, position=(0, 0), rotation=0.0, scale=(1, 1)):
        self.id = GameObject.__new_id()
        self.name = ''
        self.tags = []
        self.enabled = True
        self.visible = True
        self.static = False

        self.__children = WeakList()
        self.__parent = None

        self.__x, self.__y = position
        self.__rotation = rotation
        self.__scale = scale

        self.collider = None

    def __del__(self):
        del self.collider

    # PARENTING ===============================================================
    def add_child(self, child, cascade=True):
        if cascade: child.set_parent(self, False)
        # self.__children.append(weakref.ref(child))
        self.__children.append(child)

    def remove_child(self, child, cascade=True):
        if cascade: child.set_parent(None, False)
        # self.__children.remove(weakref.ref(child))
        self.__children.remove(child)

    def get_children(self):
        return self.__children.to_list()
        # result = []
        # for i in reversed(xrange(len(self.__children))):
        #     c = self.__children[i]()
        #     if c is None:
        #         del self.__children[i]
        #     else:
        #         result.insert(0, c)

        # return result
    children = property(get_children)

    def get_parent(self):
        if self.__parent is None: 
            return None
        return self.__parent()
    def set_parent(self, value, cascade=True):
        if cascade:
            if self.parent is not None : 
                self.parent.remove_child(self, False)
            if value is not None:
                value.add_child(self, False)

        if value is not None:
            self.__parent = weakref.ref(value)
        else:
            self.__parent = value
    parent = property(get_parent, set_parent)

    def __contains__(self, child):
        return child in self.get_children()
    # =========================================================================

    # COLLISION ===============================================================
    def add_circle_collider(self, position=None, radius=None):
        if position is None:
            position = self.position

        if radius is None:
            radius = 1

        self.collider = batma.CircleCollider(position, radius)

    def add_box_collider(self, position=None, half_width=None, half_height=None):
        if position is None:
            position = self.position

        if half_width is None:
            half_width = 1

        if half_height is None:
            half_height = 1

        self.collider = batma.BoxCollider(position, half_width, half_height)
    # =========================================================================

    # SPATIAL =================================================================
    def get_x(self):
        return self.__x
    def set_x(self, value):
        if self.collider:
            delta = value - self.__x
            self.collider.x += delta
        self.__x = value
    x = property(get_x, set_x)

    def get_y(self):
        return self.__y
    def set_y(self, value):
        if self.collider:
            delta = value - self.__y
            self.collider.y += delta
        self.__y = value
    y = property(get_y, set_y)

    def get_position(self):
        return Vector2(self.__x, self.__y)
    def set_position(self, value):
        self.x = value[0]
        self.y = value[1]
    position = property(get_position, set_position)

    def get_rotation(self):
        return self.__rotation
    def set_rotation(self, value):
        self.__rotation = value%360
    rotation = property(get_rotation, set_rotation)

    def get_scale(self):
        return self.__scale
    def set_scale(self, value):
        if isinstance(value, (int, long, float)):
            value = Vector2(value, value)
        self.__scale = value
    scale = property(get_scale, set_scale)

    def transform(self):
        gl.glTranslatef(self.x, self.y, 0)

        if self.rotation != 0.0:
            gl.glRotatef(self.rotation, 0, 0, -1)

        if self.scale != (1.0, 1.0):
            gl.glScalef(self.scale[0], self.scale[1], 0)
    # =========================================================================

    def update(self, tick):
        pass

    def draw(self):
        pass
        
    def __repr__(self): return '<GameObject "%s">'%(self.name or self.id)

if __name__ == '__main__':
    a = GameObject()
    b = GameObject()
    c = GameObject()
    a.add_child(b)
    a.add_child(c)

    print a, ':'
    print '\t', a.children

    a.remove_child(b)

    print a, ':'
    print '\t', a.children