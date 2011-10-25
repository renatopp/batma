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

"""
Example of usage::

    draw.point(Vector2(10, 20))
    draw.line(Vector2(0, 0), Vector2(640, 480))
    draw.circle((320, 240), 20)
    draw.triangle([200, 200], [250, 300], [300, 200])
"""

import pyglet
import math
from batma.algebra import Vector2

def __draw(vertices, mode):
    v = []
    for vertex in vertices:
        v.append(vertex[0])
        v.append(vertex[1])

    pyglet.graphics.draw(len(vertices), mode, ('v2f', v))

def point(*vertices):
    __draw(vertices, pyglet.gl.GL_POINTS)

def line(*vertices):
    __draw(vertices, pyglet.gl.GL_LINES)

def line_strip(*vertices):
    __draw(vertices, pyglet.gl.GL_LINE_STRIP)

def line_loop(*vertices):
    __draw(vertices, pyglet.gl.GL_LINE_LOOP)

def triangle(*vertices):
    __draw(vertices, pyglet.gl.GL_TRIANGLES)

def triangle_strip(*vertices):
    __draw(vertices, pyglet.gl.GL_TRIANGLE_STRIP)

def triangle_fan(*vertices):
    __draw(vertices, pyglet.gl.GL_TRIANGLE_FAN)

def quad(*vertices):
    __draw(vertices, pyglet.gl.GL_QUADS)

def quad_strip(*vertices):
    __draw(vertices, pyglet.gl.GL_QUAD_STRIP)

def polygon(*vertices):
    __draw(vertices, pyglet.gl.GL_POLYGON)

def circle(center, radius, faces=16):
    vertices = []
    angle, step = 0, math.pi/faces
    while angle < 2*math.pi:
        d = Vector2(radius*math.sin(angle), radius*math.cos(angle))
        vertices.append(center+d)
        angle += step
    
    line_loop(*vertices)

def rectangle(p1, p2):
    vertices = [p1, Vector2(p1[0], p2[1]), p2, Vector2(p2[0], p1[1])]
    line_loop(*vertices)
