import batma

class MyGame(batma.Game):
    def initialize(self):
        self.circle_position = (0, 0)
        self.circle_radius = 40
    
    def load_content(self):
        pass

    def update(self, tick):
        self.circle_position = self.mouse.position
        
        if self.keyboard[batma.keys.UP]:
            self.circle_radius += 1
        if self.keyboard[batma.keys.DOWN]:
            self.circle_radius -= 1
    
    def draw(self):
        batma.draw.circle(self.circle_position, self.circle_radius)

game = MyGame()
batma.run()