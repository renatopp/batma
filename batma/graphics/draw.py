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

import pygame
import batma

def rect(rect, color=None, width=0):
    '''Draws a rectangular shape'''
    color = color or batma.display.default_color
    pygame.draw.rect(batma.display.screen, color, rect, width)

def polygon(points, color=None, width=0):
    '''Draws a polygonal shape'''
    color = color or batma.display.default_color
    pygame.draw.polygon(batma.display.screen, color, points, width)

def circle(pos, radius, color=None, width=0):
    '''Draws a circular shape'''
    color = color or batma.display.default_color
    pygame.draw.circle(batma.display.screen, color, pos, radius, width)

def ellipse(rect, color=None, width=0):
    '''Draws an elliptical shape'''
    color = color or batma.display.default_color
    pygame.draw.ellipse(batma.display.screen, color, rect, width)

def arc(rect, start_angle, stop_angle, color=None, width=1):
    '''Draws an elliptical arc'''
    color = color or batma.display.default_color
    pygame.draw.arc(batma.display.screen, color, rect, start_angle, stop_angle, width)

def line(start_pos, end_pos, color=None, width=1):
    '''Draw a straight line segment'''
    color = color or batma.display.default_color
    pygame.draw.line(batma.display.screen, color, start_pos, end_pos, width)

def lines(points, closed, color=None, width=1):
    '''Draw a sequence of lines'''
    color = color or batma.display.default_color
    pygame.draw.lines(batma.display.screen, color, closed, points, width)

def aaline(start_pos, end_pos, color=None, blend=1):
    '''Draws an anti-aliased line'''
    color = color or batma.display.default_color
    pygame.draw.aaline(batma.display.screen, color, start_pos, end_pos, blend)

def aalines(points, closed, color=None, blend=1):
    '''Draws a sequence'''
    color = color or batma.display.default_color
    pygame.draw.aalines(batma.display.screen, color, closed, points, blend)