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

"""Draw directives

All methods of this module draw directly on screen.

Example of usage::

    draw.point(Vector2(10, 20))
    draw.line(Vector2(0, 0), Vector2(640, 480))
    draw.circle((320, 240), 20)
    draw.triangle([200, 200], [250, 300], [300, 200])
"""

import pyglet
import math
import batma
from batma.algebra import Vector2

def __draw(vertices, mode, width=1, color=batma.colors.BLACK):
    pyglet.gl.glLineWidth(width)
    pyglet.gl.glColor3f(*color)
    v = []
    for vertex in vertices:
        v.append(vertex[0])
        v.append(vertex[1])

    pyglet.graphics.draw(len(vertices), mode, ('v2f', v))

def point(*vertices, **kwargs):
    '''Receive a list of vertices and draw the points.

    This function uses the GL_POINT mode to draw.

    :param vertices: list of vertices, it can be a tuple, list or 
                     :py:class:`batma.algebra.Vector2`.
    :param width: an integer with the points width.
    :param color: the color of points. E.g. (0, 0, 255) or 
                  :py:const:`batma.colors.BLUE`.
    '''
    __draw(vertices, pyglet.gl.GL_POINTS, **kwargs)

def line(*vertices, **kwargs):
    '''Receive a list of vertices and draw the lines. 

    This function uses the GL_LINE mode to draw.

    Vertices list length always must be multiple of 2. E.g.::

        line((point1), (point2), (point1), (point2)) # draw 2 lines

    :param vertices: list of vertices, it can be a tuple, list or 
                     :py:class:`batma.algebra.Vector2`.
    :param width: an integer with the lines width.
    :param color: the color of lines. E.g. (0, 0, 255) or 
                  :py:const:`batma.colors.BLUE`.
    '''
    __draw(vertices, pyglet.gl.GL_LINES, **kwargs)

def line_strip(*vertices, **kwargs):
    '''Receive a list of vertices and draw the lines. 

    This function uses the GL_LINE_STRIP mode to draw.

    :param vertices: list of vertices, it can be a tuple, list or 
                     :py:class:`batma.algebra.Vector2`.
    :param width: an integer with the lines width.
    :param color: the color of lines. E.g. (0, 0, 255) or 
                  :py:const:`batma.colors.BLUE`.
    '''
    __draw(vertices, pyglet.gl.GL_LINE_STRIP, **kwargs)

def line_loop(*vertices, **kwargs):
    '''Receive a list of vertices and draw the lines. 

    This function uses the GL_LINE_LOOP mode to draw.

    :param vertices: list of vertices, it can be a tuple, list or 
                     :py:class:`batma.algebra.Vector2`.
    :param width: an integer with the lines width.
    :param color: the color of lines. E.g. (0, 0, 255) or 
                  :py:const:`batma.colors.BLUE`.
    '''
    __draw(vertices, pyglet.gl.GL_LINE_LOOP, **kwargs)

def triangle(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_TRIANGLES, **kwargs)

def triangle_strip(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_TRIANGLE_STRIP, **kwargs)

def triangle_fan(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_TRIANGLE_FAN, **kwargs)

def quad(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_QUADS, **kwargs)

def quad_strip(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_QUAD_STRIP, **kwargs)

def polygon(*vertices, **kwargs):
    __draw(vertices, pyglet.gl.GL_POLYGON, **kwargs)


def circle(center, radius, faces=16, fill=False, **kwargs):
    vertices = []
    angle, step = 0, math.pi/faces
    while angle < 2*math.pi:
        d = Vector2(radius*math.sin(angle), radius*math.cos(angle))
        vertices.append(center+d)
        angle += step
    
    if fill:
        polygon(*vertices, **kwargs)
    else:
        line_loop(*vertices, **kwargs)


def rectangle(p1, p2, fill=False, **kwargs):
    vertices = [p1, Vector2(p1[0], p2[1]), p2, Vector2(p2[0], p1[1])]

    if fill:
        polygon(*vertices, **kwargs)
    else:
        line_loop(*vertices, **kwargs)
