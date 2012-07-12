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

'''Module for color constants'''

__all__ = ['Color']

import pygame
import random
from batma.maths.algebra import Vector3
from batma.util import classproperty

class Color(list):
    def __init__(self, r, g, b, a=1.0):
        super(Color, self).__init__((r, g, b, a))

    def get_r(self):
        return self[0]
    def set_r(self, value):
        self[0] = value
    r = property(get_r, set_r)

    def get_g(self):
        return self[1]
    def set_g(self, value):
        self[1] = value
    g = property(get_g, set_g)

    def get_b(self):
        return self[2]
    def set_b(self, value):
        self[2] = value
    b = property(get_b, set_b)

    def get_a(self):
        return self[3]
    def set_a(self, value):
        self[3] = value
    a = property(get_a, set_a)

    def __repr__(self):
        return '<Color (%.2f, %.2f, %.2f, %.2f)>'%(self[0], self[1], self[2], self[3]
        )
    __str__ = __repr__

    def __add__(self, other): return Color(*[self[i]+other[i] for i in xrange(4)])
    def __sub__(self, other): return Color(*[self[i]-other[i] for i in xrange(4)])
    def __mul__(self, other): return Color(*[self[i]*other for i in xrange(4)])

    def to_pygame(self):
        return pygame.Color(
            int(self[0]*255),
            int(self[1]*255),
            int(self[2]*255),
            int(self[3]*255)
        )

    @classmethod
    def from_bytes(cls, r, g, b, a=255):
        return Color(r/255.0, g/255.0, b/255.0, a/255.0)

    @classmethod
    def random(cls):
        return Color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )


ALICE_BLUE                  = Color.from_bytes(240, 248, 255, 255)
ANTIQUE_WHITE               = Color.from_bytes(250, 235, 215, 255)
AQUA                        = Color.from_bytes(  0, 255, 255, 255)
AQUAMARINE                  = Color.from_bytes(127, 255, 212, 255)
AZURE                       = Color.from_bytes(240, 255, 255, 255)
BEIGE                       = Color.from_bytes(245, 245, 220, 255)
BISQUE                      = Color.from_bytes(255, 228, 196, 255)
BLACK                       = Color.from_bytes(  0,   0,   0, 255)
BLANCHED_ALMOND             = Color.from_bytes(255, 235, 205, 255)
BLUE                        = Color.from_bytes(  0,   0, 255, 255)
BLUE_VIOLET                 = Color.from_bytes(138,  43, 226, 255)
BROWN                       = Color.from_bytes(165,  42,  42, 255)
BURLY_WOOD                  = Color.from_bytes(222, 184, 135, 255)
CADET_BLUE                  = Color.from_bytes( 95, 158, 160, 255)
CHARTREUSE                  = Color.from_bytes(127, 255,   0, 255)
CHOCOLATE                   = Color.from_bytes(210, 105,  30, 255)
CORNFLOWER_BLUE             = Color.from_bytes(100, 149, 237, 255)
CORNSILK                    = Color.from_bytes(255, 248, 220, 255)
CRIMSOM                     = Color.from_bytes(220,  20,  60, 255)
CYAN                        = Color.from_bytes(  0, 255, 255, 255)
DARK_BLUE                   = Color.from_bytes(  0,   0, 139, 255)
DARK_CYAN                   = Color.from_bytes(  0, 139, 139, 255)
DARK_GOLDENROD              = Color.from_bytes(184, 134,  11, 255)
DARK_GRAY                   = Color.from_bytes( 64,  64,  64, 255)
DARK_GREEN                  = Color.from_bytes(  0, 100,   0, 255)
DARK_KHAKI                  = Color.from_bytes(189, 183, 107, 255)
DARK_MAGENTA                = Color.from_bytes(139,   0, 139, 255)
DARK_OLIVE_GREEN            = Color.from_bytes( 85, 107,  47, 255)
DARK_ORANGE                 = Color.from_bytes(255, 140,   0, 255)
DARK_ORCHID                 = Color.from_bytes(153,  50, 204, 255)
DARK_RED                    = Color.from_bytes(139,   0,   0, 255)
DARK_SALMAN                 = Color.from_bytes(233, 150, 122, 255)
DARK_SEA_GREEN              = Color.from_bytes(143, 188, 139, 255)
DARK_SLATE_BLUE             = Color.from_bytes( 72,  61, 139, 255)
DARK_SLATE_GRAY             = Color.from_bytes( 47,  79,  79, 255)
DARK_TURQUOISE              = Color.from_bytes(  0, 206, 209, 255)
DARK_VIOLET                 = Color.from_bytes(148,   0, 211, 255)
DEEP_PINK                   = Color.from_bytes(255,  20, 147, 255)
DEEP_SKY_BLUE               = Color.from_bytes(  0, 191, 255, 255)
DIM_GRAY                    = Color.from_bytes(105, 105, 105, 255)
DODGER_BLUE                 = Color.from_bytes( 30, 144, 255, 255)
FIRE_BRICK                  = Color.from_bytes(178,  34,  34, 255)
FLORAL_WHITE                = Color.from_bytes(255, 250, 240, 255)
FOREST_GREEN                = Color.from_bytes( 34, 139,  34, 255)
FUCHSIA                     = Color.from_bytes(255,   0, 255, 255)
GAINSBORO                   = Color.from_bytes(220, 220, 220, 255)
GHOST_WHITE                 = Color.from_bytes(248, 248, 255, 255)
GOLD                        = Color.from_bytes(255, 215,   0, 255)
GOLDNROD                    = Color.from_bytes(218, 165,  32, 255)
GRAY                        = Color.from_bytes(128, 128, 128, 255)
GREEN                       = Color.from_bytes(  0, 255,   0, 255)
GREEN_YELLOW                = Color.from_bytes(173, 255,  47, 255)
HONEYDEW                    = Color.from_bytes(240, 255, 240, 255)
HOT_PINK                    = Color.from_bytes(255, 105, 180, 255)
INDIAN_RED                  = Color.from_bytes(205,  92,  92, 255)
INDIGO                      = Color.from_bytes( 75,   0, 130, 255)
IVORY                       = Color.from_bytes(255, 255, 240, 255)
KHAKI                       = Color.from_bytes(240, 230, 140, 255)
LAVENDER                    = Color.from_bytes(230, 230, 250, 255)
LAVANDER_BLUE               = Color.from_bytes(204, 204, 255, 255)
LAVENDER_BLUSH              = Color.from_bytes(255, 240, 245, 255)
LAWN_GREEN                  = Color.from_bytes(124, 252,   0, 255)
LEMON_CHIFFON               = Color.from_bytes(255, 250, 205, 255)
LIGHT_BLUE                  = Color.from_bytes(173, 216, 230, 255)
LIGHT_CORAL                 = Color.from_bytes(240, 128, 128, 255)
LIGHT_CYAN                  = Color.from_bytes(224, 255, 255, 255)
LIGHT_FRENCH_LAVANDER       = Color.from_bytes(168, 153, 230, 255)
LIGHT_GOLDENROD_YELLOW      = Color.from_bytes(250, 250, 210, 255)
LIGHT_GRAY                  = Color.from_bytes(211, 211, 211, 255)
LIGHT_GREEN                 = Color.from_bytes(144, 238, 144, 255)
LIGHT_PINK                  = Color.from_bytes(255, 182, 193, 255)
LIGHT_SALMON                = Color.from_bytes(255, 160, 122, 255)
LIGHT_SEA_GREEN             = Color.from_bytes( 32, 178, 170, 255)
LIGHT_SKY_BLUE              = Color.from_bytes(135, 206, 250, 255)
LIGHT_SLATE_GRAY            = Color.from_bytes(119, 136, 153, 255)
LIGHT_STEEL_BLUE            = Color.from_bytes(176, 196, 222, 255)
LIGHT_YELLOW                = Color.from_bytes(255, 255, 224, 255)
LIME                        = Color.from_bytes(  0, 255,   0, 255)
LIME_GREEN                  = Color.from_bytes( 50, 205,  50, 255)
LINEN                       = Color.from_bytes(250, 240, 230, 255)
MAGENTA                     = Color.from_bytes(255,   0, 255, 255)
MAROON                      = Color.from_bytes(128,   0,   0, 255)
MEDIUM_AQUAMARINE           = Color.from_bytes(102, 205, 170, 255)
MEDIUM_BLUE                 = Color.from_bytes(  0,   0, 205, 255)
MEDIUM_ORCHID               = Color.from_bytes(186,  85, 211, 255)
MEDIUM_PURPLE               = Color.from_bytes(147, 112, 219, 255)
MEDIUM_SEA_GREEN            = Color.from_bytes( 60, 179, 113, 255)
MEDIUM_SLATE_BLUE           = Color.from_bytes(123, 104, 238, 255)
MEDIUM_SPRING_GREEN         = Color.from_bytes(  0, 250, 154, 255)
MEDIUM_TURQUOISE            = Color.from_bytes( 72, 209, 204, 255)
MEDIUM_VIOLETRED            = Color.from_bytes(199,  21, 133, 255)
MIDNIGHT_BLUE               = Color.from_bytes( 25,  25, 112, 255)
MINT_CREAM                  = Color.from_bytes(245, 255, 250, 255)
MISTY_ROSE                  = Color.from_bytes(255, 228, 225, 255)
MOCCASIN                    = Color.from_bytes(255, 228, 181, 255)
NAVAJO_WHITE                = Color.from_bytes(255, 222, 173, 255)
NAVY                        = Color.from_bytes(  0,   0, 128, 255)
OLD_LACE                    = Color.from_bytes(253, 245, 230, 255)
OLIVE                       = Color.from_bytes(128, 128,   0, 255)
OLIVE_DRAB                  = Color.from_bytes(107, 142,  35, 255)
ORANGE                      = Color.from_bytes(255, 165,   0, 255)
ORANGE_RED                  = Color.from_bytes(255,  69,   0, 255)
ORCHID                      = Color.from_bytes(218, 112, 214, 255)
PALE_GOLDENROD              = Color.from_bytes(238, 232, 170, 255)
PALE_GREEN                  = Color.from_bytes(152, 251, 152, 255)
PALE_TURQUOISE              = Color.from_bytes(175, 238, 238, 255)
PALE_VIOLET_RED             = Color.from_bytes(219, 112, 147, 255)
PAPAYA_WHIP                 = Color.from_bytes(255, 239, 213, 255)
PEACH_PUFF                  = Color.from_bytes(255, 218, 185, 255)
PERIWINKLE                  = Color.from_bytes(204, 204, 255, 255)
PERU                        = Color.from_bytes(205, 133,  63, 255)
PINK                        = Color.from_bytes(255, 192, 203, 255)
PLUM                        = Color.from_bytes(221, 160, 221, 255)
POWDER_BLUE                 = Color.from_bytes(176, 224, 230, 255)
PURPLE                      = Color.from_bytes(128,   0, 128, 255)
RED                         = Color.from_bytes(255,   0,   0, 255)
ROSY_BROWN                  = Color.from_bytes(188, 143, 143, 255)
ROYAL_BLUE                  = Color.from_bytes( 65, 105, 225, 255)
SADDLE_BROWN                = Color.from_bytes(139,  69,  19, 255)
SALMON                      = Color.from_bytes(250, 128, 114, 255)
SANDY_BROWN                 = Color.from_bytes(244, 164,  96, 255)
SEA_GREEN                   = Color.from_bytes( 46, 139,  87, 255)
SEA_SHELL                   = Color.from_bytes(255, 245, 238, 255)
SIENNA                      = Color.from_bytes(160,  82,  45, 255)
SILVER                      = Color.from_bytes(192, 192, 192, 255)
SKY_BLUE                    = Color.from_bytes(135, 206, 235, 255)
SLATE_BLUE                  = Color.from_bytes(106,  90, 205, 255)
SLATE_GRAY                  = Color.from_bytes(112, 128, 144, 255)
SNOW                        = Color.from_bytes(255, 250, 250, 255)
SPRING_GREEN                = Color.from_bytes(  0, 255, 127, 255)
STEEL_BLUE                  = Color.from_bytes( 70, 130, 180, 255)
TAN                         = Color.from_bytes(210, 180, 140, 255)
TEAL                        = Color.from_bytes(  0, 128, 128, 255)
THISTLE                     = Color.from_bytes(216, 191, 216, 255)
TOMATO                      = Color.from_bytes(255,  99,  71, 255)
TRANSPARENT                 = Color.from_bytes(  0,   0,   0,   0)
TURQUOISE                   = Color.from_bytes( 64, 224, 208, 255)
VIOLET                      = Color.from_bytes(238, 130, 238, 255)
WHEAT                       = Color.from_bytes(245, 222, 179, 255)
WHITE                       = Color.from_bytes(255, 255, 255, 255)
WHITE_SMOKE                 = Color.from_bytes(245, 245, 245, 255)
YELLOW                      = Color.from_bytes(255, 255,   0, 255)
YELLOW_GREEN                = Color.from_bytes(154, 205,  50, 255)