import batma

from models import *

class Lose(batma.Scene):
    def load_content(self):
        self.label = batma.Text('Loser...', batma.display.center)

    def update(self, tick):
        if batma.mouse.is_any_pressed():
            batma.game.new_game()

    def draw(self):
        self.label.draw()

class Win(batma.Scene):
    def load_content(self):
        self.label = batma.Text('Winner!', batma.display.center)

    def update(self, tick):
        if batma.mouse.is_any_pressed():
            batma.game.new_game()

    def draw(self):
        self.label.draw()

class LevelScene(batma.Scene):
    def initialize(self):
        self.level = batma.game.level
        self.player = batma.game.player
        self.n_foes = batma.game.n_foes
        self.n_goals = batma.game.n_goals

        batma.display.show_fps = True
        # batma.display.show_colliders = True
        batma.display.show_cursor = False
        batma.display.background_color = batma.game.colors[self.level]

    def reset(self):
        self.foes.clear()
        self.goals.clear()

        for i in xrange(self.n_foes):
            self.foes.add(Foe(batma.Vector2(200, 200)))

        for i in xrange(self.n_goals):
            self.goals.append(Goal())

    def load_content(self):
        self.foes = batma.Group()
        self.goals = batma.Group()

        self.reset()

    def unload_content(self):
        pass

    def update(self, tick):
        self.player.update(tick)
        self.foes.update(tick)

        # Foe Collision
        if self.foes.any_colliding(self.player):
            self.player.life -= 1
            self.reset()

        # Goal Collision
        for obj in self.goals.objs_colliding(self.player):
            self.goals.remove(obj)
            self.n_goals -= 1

        # Win Verification
        if self.n_goals == 0:
            batma.game.next_level()

        # Lose Verification
        if self.player.life == 0:
            batma.game.lose()
        
        if batma.keyboard.is_pressed('jump'):
            print self.n_goals
    
    def draw(self):
        self.goals.draw()
        self.foes.draw()
        self.player.draw()