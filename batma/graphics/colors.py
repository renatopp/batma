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
from batma.util import classproperty

class Color(pygame.Color):
    '''Extension of the pygame.Color'''
    @classproperty
    @classmethod
    def Random(cls):
        return Color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )


ALICE_BLUE                  = Color(240, 248, 255, 255)
ANTIQUE_WHITE               = Color(250, 235, 215, 255)
AQUA                        = Color(  0, 255, 255, 255)
AQUAMARINE                  = Color(127, 255, 212, 255)
AZURE                       = Color(240, 255, 255, 255)
        
BEIGE                       = Color(245, 245, 220, 255)
BISQUE                      = Color(255, 228, 196, 255)
BLACK                       = Color(  0,   0,   0, 255)
BLANCHED_ALMOND             = Color(255, 235, 205, 255)
BLUE                        = Color(  0,   0, 255, 255)
BLUE_VIOLET                 = Color(138,  43, 226, 255)
BROWN                       = Color(165,  42,  42, 255)
BURLY_WOOD                  = Color(222, 184, 135, 255)
        
CADET_BLUE                  = Color( 95, 158, 160, 255)
CHARTREUSE                  = Color(127, 255,   0, 255)
CHOCOLATE                   = Color(210, 105,  30, 255)
CORNFLOWER_BLUE             = Color(100, 149, 237, 255)
CORNSILK                    = Color(255, 248, 220, 255)
CRIMSOM                     = Color(220,  20,  60, 255)
CYAN                        = Color(  0, 255, 255, 255)
        
DARK_BLUE                   = Color(  0,   0, 139, 255)
DARK_CYAN                   = Color(  0, 139, 139, 255)
DARK_GOLDENROD              = Color(184, 134,  11, 255)
DARK_GRAY                   = Color( 64,  64,  64, 255)
DARK_GREEN                  = Color(  0, 100,   0, 255)
DARK_KHAKI                  = Color(189, 183, 107, 255)
DARK_MAGENTA                = Color(139,   0, 139, 255)
DARK_OLIVE_GREEN            = Color( 85, 107,  47, 255)
DARK_ORANGE                 = Color(255, 140,   0, 255)
DARK_ORCHID                 = Color(153,  50, 204, 255)
DARK_RED                    = Color(139,   0,   0, 255)
DARK_SALMAN                 = Color(233, 150, 122, 255)
DARK_SEA_GREEN              = Color(143, 188, 139, 255)
DARK_SLATE_BLUE             = Color( 72,  61, 139, 255)
DARK_SLATE_GRAY             = Color( 47,  79,  79, 255)
DARK_TURQUOISE              = Color(  0, 206, 209, 255)
DARK_VIOLET                 = Color(148,   0, 211, 255)
DEEP_PINK                   = Color(255,  20, 147, 255)
DEEP_SKY_BLUE               = Color(  0, 191, 255, 255)
DIM_GRAY                    = Color(105, 105, 105, 255)
DODGER_BLUE                 = Color( 30, 144, 255, 255)
        
FIRE_BRICK                  = Color(178,  34,  34, 255)
FLORAL_WHITE                = Color(255, 250, 240, 255)
FOREST_GREEN                = Color( 34, 139,  34, 255)
FUCHSIA                     = Color(255,   0, 255, 255)
        
GAINSBORO                   = Color(220, 220, 220, 255)
GHOST_WHITE                 = Color(248, 248, 255, 255)
GOLD                        = Color(255, 215,   0, 255)
GOLDNROD                    = Color(218, 165,  32, 255)
GRAY                        = Color(128, 128, 128, 255)
GREEN                       = Color(  0, 255,   0, 255)
GREEN_YELLOW                = Color(173, 255,  47, 255)
        
HONEYDEW                    = Color(240, 255, 240, 255)
HOT_PINK                    = Color(255, 105, 180, 255)
        
INDIAN_RED                  = Color(205,  92,  92, 255)
INDIGO                      = Color( 75,   0, 130, 255)
IVORY                       = Color(255, 255, 240, 255)
        
KHAKI                       = Color(240, 230, 140, 255)
LAVENDER                    = Color(230, 230, 250, 255)
LAVANDER_BLUE               = Color(204, 204, 255, 255)
LAVENDER_BLUSH              = Color(255, 240, 245, 255)
LAWN_GREEN                  = Color(124, 252,   0, 255)
LEMON_CHIFFON               = Color(255, 250, 205, 255)

LIGHT_BLUE                  = Color(173, 216, 230, 255)
LIGHT_CORAL                 = Color(240, 128, 128, 255)
LIGHT_CYAN                  = Color(224, 255, 255, 255)
LIGHT_FRENCH_LAVANDER       = Color(168, 153, 230, 255)
LIGHT_GOLDENROD_YELLOW      = Color(250, 250, 210, 255)
LIGHT_GRAY                  = Color(211, 211, 211, 255)
LIGHT_GREEN                 = Color(144, 238, 144, 255)
LIGHT_PINK                  = Color(255, 182, 193, 255)
LIGHT_SALMON                = Color(255, 160, 122, 255)
LIGHT_SEA_GREEN             = Color( 32, 178, 170, 255)
LIGHT_SKY_BLUE              = Color(135, 206, 250, 255)
LIGHT_SLATE_GRAY            = Color(119, 136, 153, 255)
LIGHT_STEEL_BLUE            = Color(176, 196, 222, 255)
LIGHT_YELLOW                = Color(255, 255, 224, 255)
LIME                        = Color(  0, 255,   0, 255)
LIME_GREEN                  = Color( 50, 205,  50, 255)
LINEN                       = Color(250, 240, 230, 255)

MAGENTA                     = Color(255,   0, 255, 255)
MAROON                      = Color(128,   0,   0, 255)
MEDIUM_AQUAMARINE           = Color(102, 205, 170, 255)
MEDIUM_BLUE                 = Color(  0,   0, 205, 255)
MEDIUM_ORCHID               = Color(186,  85, 211, 255)
MEDIUM_PURPLE               = Color(147, 112, 219, 255)
MEDIUM_SEA_GREEN            = Color( 60, 179, 113, 255)
MEDIUM_SLATE_BLUE           = Color(123, 104, 238, 255)
MEDIUM_SPRING_GREEN         = Color(  0, 250, 154, 255)
MEDIUM_TURQUOISE            = Color( 72, 209, 204, 255)
MEDIUM_VIOLETRED            = Color(199,  21, 133, 255)
MIDNIGHT_BLUE               = Color( 25,  25, 112, 255)
MINT_CREAM                  = Color(245, 255, 250, 255)
MISTY_ROSE                  = Color(255, 228, 225, 255)
MOCCASIN                    = Color(255, 228, 181, 255)

NAVAJO_WHITE                = Color(255, 222, 173, 255)
NAVY                        = Color(  0,   0, 128, 255)

OLD_LACE                    = Color(253, 245, 230, 255)
OLIVE                       = Color(128, 128,   0, 255)
OLIVE_DRAB                  = Color(107, 142,  35, 255)
ORANGE                      = Color(255, 165,   0, 255)
ORANGE_RED                  = Color(255,  69,   0, 255)
ORCHID                      = Color(218, 112, 214, 255)

PALE_GOLDENROD              = Color(238, 232, 170, 255)
PALE_GREEN                  = Color(152, 251, 152, 255)
PALE_TURQUOISE              = Color(175, 238, 238, 255)
PALE_VIOLET_RED             = Color(219, 112, 147, 255)
PAPAYA_WHIP                 = Color(255, 239, 213, 255)
PEACH_PUFF                  = Color(255, 218, 185, 255)
PERIWINKLE                  = Color(204, 204, 255, 255)
PERU                        = Color(205, 133,  63, 255)
PINK                        = Color(255, 192, 203, 255)
PLUM                        = Color(221, 160, 221, 255)
POWDER_BLUE                 = Color(176, 224, 230, 255)
PURPLE                      = Color(128,   0, 128, 255)

RED                         = Color(255,   0,   0, 255)
ROSY_BROWN                  = Color(188, 143, 143, 255)
ROYAL_BLUE                  = Color( 65, 105, 225, 255)

SADDLE_BROWN                = Color(139,  69,  19, 255)
SALMON                      = Color(250, 128, 114, 255)
SANDY_BROWN                 = Color(244, 164,  96, 255)
SEA_GREEN                   = Color( 46, 139,  87, 255)
SEA_SHELL                   = Color(255, 245, 238, 255)
SIENNA                      = Color(160,  82,  45, 255)
SILVER                      = Color(192, 192, 192, 255)
SKY_BLUE                    = Color(135, 206, 235, 255)
SLATE_BLUE                  = Color(106,  90, 205, 255)
SLATE_GRAY                  = Color(112, 128, 144, 255)
SNOW                        = Color(255, 250, 250, 255)
SPRING_GREEN                = Color(  0, 255, 127, 255)
STEEL_BLUE                  = Color( 70, 130, 180, 255)

TAN                         = Color(210, 180, 140, 255)
TEAL                        = Color(  0, 128, 128, 255)
THISTLE                     = Color(216, 191, 216, 255)
TOMATO                      = Color(255,  99,  71, 255)
TRANSPARENT                 = Color(  0,   0,   0,   0)
TURQUOISE                   = Color( 64, 224, 208, 255)

VIOLET                      = Color(238, 130, 238, 255)

WHEAT                       = Color(245, 222, 179, 255)
WHITE                       = Color(255, 255, 255, 255)
WHITE_SMOKE                 = Color(245, 245, 245, 255)

YELLOW                      = Color(255, 255,   0, 255)
YELLOW_GREEN                = Color(154, 205,  50, 255)