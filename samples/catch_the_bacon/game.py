# -*- coding:utf-8 -*-

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from ctypes import util
try:
    from OpenGL.platform import win32
except AttributeError:
    pass
    
import batma
from models import *
from scenes import *

class Game(batma.Scene):    
    def load_content(self):
        self.images = {
            'troll': batma.resource.load_image('assets/troll.png'),
            'goal': batma.resource.load_image('assets/goal.png'),
            'derp5': batma.resource.load_image('assets/derp5.png'),
            'derp4': batma.resource.load_image('assets/derp4.png'),
            'derp3': batma.resource.load_image('assets/derp3.png'),
            'derp2': batma.resource.load_image('assets/derp2.png'),
            'derp1': batma.resource.load_image('assets/derp1.png'),
            'derp0': batma.resource.load_image('assets/derp1.png'),
        }
        self.colors = [
            batma.colors.WHITE,
            batma.colors.BLUE,
            batma.colors.GREEN,
            batma.colors.YELLOW,
            batma.colors.RED
        ]
        self.player = Player(5)
        self.level = 0
        self.n_goals = 10
        self.n_foes = 10
        self.n_levels = 5

        self.new_game()

    def update(self, tick):
        if batma.keyboard.is_released('quit'):
            batma.engine.stop()

    def new_game(self):
        self.player.life = 5
        self.level = 0
        self.add_scene(LevelScene())

    def next_level(self):
        self.level += 1
        if self.level >= self.n_levels:
            self.win()
        else:
            self.add_scene(LevelScene())

    def win(self):
        self.add_scene(Win())

    def lose(self):
        self.add_scene(Lose())

game = Game()
batma.run(game)