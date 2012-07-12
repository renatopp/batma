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

'''Module for drawing primitives'''

import pygame
import batma
from batma.maths import mathematic as math
from OpenGL import GL as gl

def point(position, color=None):
    color = color or batma.display.default_color
    gl.glDisable(gl.GL_TEXTURE_2D)
    
    gl.glColor4fv(color)

    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(*position)
    gl.glEnd()
    
    gl.glEnable(gl.GL_TEXTURE_2D)

def points(points, color=None):
    color = color or batma.display.default_color
    gl.glDisable(gl.GL_TEXTURE_2D)
    
    gl.glColor4fv(color)

    gl.glBegin(gl.GL_POINTS)
    for position in points:
        gl.glVertex2f(*position)
    gl.glEnd()
    
    gl.glEnable(gl.GL_TEXTURE_2D)

def line(start_pos, end_pos, color=None, width=1):
    color = color or batma.display.default_color
    gl.glDisable(gl.GL_TEXTURE_2D)

    gl.glLineWidth(width)
    gl.glColor4fv(color)
    
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(*start_pos)
    gl.glVertex2f(*end_pos)
    gl.glEnd()
    
    gl.glEnable(gl.GL_TEXTURE_2D)

def lines(points, closed=False, color=None, width=1):
    color = color or batma.display.default_color
    gl.glDisable(gl.GL_TEXTURE_2D)

    gl.glLineWidth(width)
    gl.glColor4fv(color)
    
    gl.glBegin(gl.GL_LINE_LOOP if closed else gl.GL_LINE_STRIP)
    for position in points:
        gl.glVertex2f(*position)
    gl.glEnd()
    
    gl.glEnable(gl.GL_TEXTURE_2D)

def polygon(points, color=None, width=0):
    color = color or batma.display.default_color
    gl.glDisable(gl.GL_TEXTURE_2D)

    gl.glLineWidth(width or 1)
    gl.glColor4fv(color)
    
    gl.glBegin(gl.GL_POLYGON if width==0 else gl.GL_LINE_LOOP)
    for position in points:
        gl.glVertex2f(*position)
    gl.glEnd()
    
    gl.glEnable(gl.GL_TEXTURE_2D)

def circle(center, radius, color=None, width=0):
    points = []
    x, y = center
    angle, step = 0, math.pi/18

    while angle < 2*math.pi:
        dx, dy = (radius*math.sin(angle), radius*math.cos(angle))
        points.append((x+dx, y+dy))
        angle += step
    
    polygon(points, color, width)

def rect(rect, color=None, width=0):
    x, y, w, h = rect
    points = (
        (x, y),
        (x+w, y),
        (x+w, y+h),
        (x, y+h)
    )
    return polygon(points, color, width)

# def ellipse(rect, color=None, width=0):
#     '''Draws an elliptical shape'''
#     color = color or batma.display.default_color
#     pygame.draw.ellipse(batma.display.screen, color, rect, width)

# def arc(rect, start_angle, stop_angle, color=None, width=1):
#     '''Draws an elliptical arc'''
#     color = color or batma.display.default_color
#     pygame.draw.arc(batma.display.screen, color, rect, start_angle, stop_angle, width)
