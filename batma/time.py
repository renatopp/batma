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

__all__ = ['Clock', 'Timer']

import pygame
import batma
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

class ScheduledFunction(object):
    def __init__(self, id, function, time, is_once, args):
        self.id = id
        self.function = function
        self.time = time
        self.is_once = is_once
        self.args = args

        self.last_tick = batma.clock.get_ticks()

    def __call__(self):
        current_tick = batma.clock.get_ticks()
        time_passed = current_tick-self.last_tick
        self.last_tick = current_tick

        args, kwargs = self.args
        self.function(time_passed, *args, **kwargs)

@singleton
class Timer(object):
    def __init__(self):
        self.__userevent = pygame.USEREVENT+1
        self.__scheduled = {}

    def __schedule(self, callback, time, is_once, *args, **kwargs):
        self.__userevent += 1
        id = self.__userevent

        function = ScheduledFunction(
            id=id,
            function=callback,
            time=time,
            is_once=is_once,
            args=(args, kwargs)
        )

        self.__scheduled[id] = function
        pygame.time.set_timer(id, time)


    def schedule_once(self, callback, time, *args, **kwargs):
        self.__schedule(callback, time, True, *args, **kwargs)

    def schedule(self, callback, time, *args, **kwargs):
        self.__schedule(callback, time, False, *args, **kwargs)

    def unschedule(self, callback):
        for id in self.__scheduled:
            if self.__scheduled[id] == callback:
                self.unschedule_by_id(id)
                break

    def unschedule_by_id(self, id):
        pygame.time.set_timer(id, 0)
        del self.__scheduled[id]

    def update(self, event):
        if event.type in self.__scheduled:
            callback = self.__scheduled[event.type]
            callback()

            if callback.is_once:
                self.unschedule_by_id(callback.id)



