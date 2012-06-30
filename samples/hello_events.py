# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import batma

class Game(batma.Scene):
    def initialize(self):
        pass
    
    def load_content(self):
        pass

    def unload_content(self):
        pass

    def update(self, tick):
        if batma.keyboard.is_clicked('quit'): #ESC or ALT+F4
            batma.engine.stop()
    
    def draw(self):
        batma.draw.circle(batma.mouse.position, radius=35, width=1)

game = Game()
batma.run(game)