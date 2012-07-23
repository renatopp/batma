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
from batma.util import singleton, WeakList

@singleton
class Engine(object):
    '''Batma Engine object'''
    def __init__(self):
        self.all_colliders = WeakList()
        self.__running = True
        self.__exit = False

    # Game Loop ===============================================================    
    def __game_loop(self):
        '''Game loop'''

        # text_fps for FPS report on screen
        # text_fps = batma.Text('', 
        #     position=(10, 10), 
        #     anchor='bottomleft',
        #     font_size=62,
        #     color=batma.Color(0.3, 0.3, 0.3, 1)
        # )

        # Initialize the game =================================================
        batma.game._initialize()
        batma.game._load_content()
        # =====================================================================
        
        batma.clock.tick(batma.display.max_fps)
        
        while not self.__exit:
            tick = batma.clock.tick(batma.display.max_fps)

            # Event Update ====================================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #
                    self.stop()
                elif event.type == pygame.VIDEORESIZE:
                    # Update the display size with the new window resolution
                    batma.display.size = event.size
                else:
                    # User defined schedule functions
                    batma.clock.update_schedule(event)
            # =================================================================

            # Input Update ====================================================
            batma.keyboard.update(tick)
            batma.mouse.update(tick)
            # =================================================================

            # Game Update and Drawing =========================================
            if self.__running:
                batma.game._update(tick)
                
                # Clear after the update, forcing all drawing call to be
                # called on game.draw()
                batma.display.clear()
                batma.game._draw()
            # =================================================================
            
            # Camera location =================================================
            batma.camera.locate()
            # =================================================================

            if batma.display.show_colliders:
                for collider in self.all_colliders.iter():
                    collider.draw()

            # if batma.display.show_fps:
            #     text_fps.text = '%.2f'%batma.clock.get_fps()
            #     text_fps.draw()
                
            pygame.display.flip()

        batma.game._unload_content()
    # =========================================================================

    # Configuration ===========================================================
    def apply_config(self, game, *args, **kwargs):
        '''Apply new configuration to engine'''

        # Set up the global variables
        batma.game = game
        batma.camera = Camera()

        # Pygame initialization
        pygame.init()
        pygame.font.init()

        # Display initialization
        batma.display.apply_config(*args, **kwargs)
    # =========================================================================

    # Engine Control ==========================================================
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
