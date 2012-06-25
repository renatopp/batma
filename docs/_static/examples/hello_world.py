import batma

class Game(batma.Game):
    def initialize(self):
        pass
    
    def load_content(self):
        self.label = batma.Label('Hello, World!', self.center)

    def update(self, tick):
        pass
    
    def draw(self):
        self.label.draw()

game = Game()
batma.run()