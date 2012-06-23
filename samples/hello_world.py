# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import batma

class Game(batma.Scene):
    def initialize(self):
        pass
    
    def load_content(self):
        self.label = batma.Text(u'Hello World!', batma.display.center)
        self.label.scale = 1

    def unload_content(self):
        pass

    def update(self, tick):
        pass
    
    def draw(self):
        self.label.draw()

game = Game()
batma.run(game)