import batma
import random

def set_position(obj):
    while True:
        obj.position = batma.util.random_position(20, 20)
        if not obj.collider.near_than(batma.game.player.collider, 50):
            return


class Foe(batma.Sprite):
    def __init__(self, speed):
        super(Foe, self).__init__(batma.game.images['troll'], scale=0.5)
        self.speed = speed
        self.direction = batma.Vector2.NormRandom
        self.add_box_collider()

        set_position(self)

    def update(self, tick):
        self.position += self.speed*self.direction*tick/1000.0

        if self.position.x+self.width/2.0 > batma.display.width:
            self.direction.x = -abs(self.direction.x)
        if self.position.x-self.width/2.0 < 0:
            self.direction.x = abs(self.direction.x)
        if self.position.y+self.height/2.0 > batma.display.height:
            self.direction.y = -abs(self.direction.y)
        if self.position.y-self.height/2.0 < 0:
            self.direction.y = abs(self.direction.y)

class Player(batma.Sprite):
    def __init__(self, life=5):
        super(Player, self).__init__(batma.game.images['derp'+str(life)], scale=0.5)
        self.add_box_collider()
        self.__life = life

    def update(self, tick):
        self.position = batma.mouse.position

    def get_life(self):
        return self.__life
    def set_life(self, value):
        self.__life = value
        self.image = batma.game.images['derp'+str(value)]
    life = property(get_life, set_life)

class Goal(batma.Sprite):
    def __init__(self):
        super(Goal, self).__init__(batma.game.images['goal'], scale=0.5)
        self.add_box_collider()
        
        set_position(self)
