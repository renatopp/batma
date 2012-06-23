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

__all__ = ['Engine']

import pygame
import batma
from batma.display import Display
from batma.input import KeyboardState, MouseState
from batma.scene import Scene
from batma.util import singleton

@singleton
class Engine(object):
    def __init__(self):
        self.__userevent = pygame.USEREVENT+1
        self.__scheduled = {} # id: function

        self._running = True
        self._exit = False
        self.game = None

    # =========================================================================    
    def __game_loop(self):
        text_fps = batma.text.Text('', font_size=62)
        text_fps.anchor = [0, 0]
        text_fps.position = (70, batma.display.height-30)
        text_fps.scale = 1

        self.game._initialize()
        self.game._load_content()

        while not self._exit:
            time_passed = batma.clock.tick(batma.display.max_fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                elif event.type in self.__scheduled:
                    function = self.__scheduled[event.type]
                    function()

            batma.keyboard.update()
            batma.mouse.update()

            batma.display.clear()
            if self._running:
                self.game._update(time_passed)
                self.game._draw()

            if batma.display.show_fps:
                text_fps.text = '%.2f'%batma.clock.get_fps()
                text_fps.draw()

            pygame.display.flip()

        self.game._unload_content()
    # =========================================================================

    # =========================================================================
    def apply_config(self, game, *args, **kwargs):
        self.game = game

        pygame.init()
        pygame.font.init()
        batma.display.apply_config(*args, **kwargs)
    # =========================================================================

    # =========================================================================
    def schedule(self, function, time):
        self.__userevent += 1
        self.__scheduled[self.__userevent] = function
        pygame.time.set_timer(self.__userevent, time)

    def unschedule(self, function):
        for id in self.__scheduled:
            if self.__scheduled[id] == function:
                pygame.time.set_timer(id, 0)
                del self.__scheduled[id]
                break
    # =========================================================================

    # =========================================================================
    def start(self):
        self._running = True
        self._exit = False

        batma.display.init()

        self.__game_loop()

    def pause(self):
        self._running = False

    def resume(self):
        self._running = True

    def stop(self):
        self._exit = True
    # =========================================================================
