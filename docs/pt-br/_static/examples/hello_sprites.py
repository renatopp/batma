import batma

class MyGame(batma.Game):
    def initialize(self):
        pass
    
    def load_content(self):
        self.sprite = batma.Sprite('python_logo.png', self.center)

    def update(self, tick):
        pass
    
    def draw(self):
        self.sprite.draw()

game = MyGame()
batma.run()