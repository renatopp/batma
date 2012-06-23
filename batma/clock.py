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

__all__ = ['Clock']

import pygame
from batma.util import singleton

@singleton
class Clock(object):
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__time_passed = 0

    def tick(self, framerate=0):
        time_passed = self.__clock.tick(framerate)
        self.__time_passed += time_passed
        return time_passed

    def tick_busy_loop(self, framerate=0):
        time_passed = self.__clock.tick(framerate)
        self.__time_passed += time_passed
        return time_passed

    def get_time(self):
        return self.__clock.get_time()

    def get_rawtime(self):
        return self.__clock.get_rawtime()

    def get_fps(self):
        return self.__clock.get_fps()

    def get_ticks(self):
        return self.__time_passed