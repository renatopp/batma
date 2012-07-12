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
from batma.core.camera import Camera
from batma.util import singleton

@singleton
class Engine(object):
    def __init__(self):
        self.__running = True
        self.__exit = False

    # =========================================================================    
    def __game_loop(self):
        text_fps = batma.Text(
            text='', 
            position=(10, 10), 
            anchor='bottomleft',
            font_size=62,
            color=batma.Color(0.3, 0.3, 0.3, 1)
        )
        # text_fps = batma.Sprite(batma.resource.Text('Hello World', fontsize=48), batma.display.center)
        # text_fps.position = (70, batma.display.height-30)

        batma.game._initialize()
        batma.game._load_content()
        
        while not self.__exit:
            time_passed = batma.clock.tick(batma.display.max_fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                elif event.type == pygame.VIDEORESIZE:
                    batma.display.size = event.size
                else:
                    batma.clock.update_schedule(event)

            batma.keyboard.update()
            batma.mouse.update()

            batma.display.clear()
            if self.__running:
                batma.game._update(time_passed)
                batma.game._draw()

            if batma.display.show_fps:
                text_fps.text = '%.2f'%batma.clock.get_fps()
                text_fps.draw()
                
            batma.camera.locate()
            pygame.display.flip()

        batma.game._unload_content()
    # =========================================================================

    # =========================================================================
    def apply_config(self, game, *args, **kwargs):
        '''Apply new configuration to engine'''
        batma.game = game

        pygame.init()
        pygame.font.init()
        batma.display.apply_config(*args, **kwargs)
        
        batma.camera = Camera()
    # =========================================================================

    # =========================================================================
    def start(self):
        '''Starts the engine'''
        self.__running = True
        self.__exit = False

        batma.display.init()

        self.__game_loop()

    def pause(self):
        '''Pauses the engine'''
        self.__running = False

    def resume(self):
        '''Resume the paused engine'''
        self.__running = True

    def stop(self):
        '''Stop the engine and end the game'''
        self.__exit = True

    def is_running(self):
        '''Verify if engine is paused'''
        return self.__running
    # =========================================================================
