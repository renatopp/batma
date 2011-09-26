========
Batma 2D
========

Batma is a pyglet based game engine, inpired by XNA's structure and cocos2d's 
features. The Batma's goal is provide an intuitive structure for game 
development and other graphical applications.


--------
Features
--------

  - Automatic import regular image atlas in a list of images
  - Animated Sprites creation from image atlas or gifs
  - Easy-to-use pyglet components, e.g., sprites, texts and resource locations
  - Input state for keyboard and mouse (also inspired by XNA)


-------------
Game Workflow
-------------

Inspired by XNA, a Batma game follows almost the same structure::

    class MyGame(batma.Game):
        def initialize(self):
            """Initializes game components, such screen properties"""
            ...
        
        def load_content(self):
            """Load game assets, such as sprites, fonts and sound effects"""
            ...
        
        def update(self, tick):
            """Called each frame, add all the game logic here"""
            ...
        
        def draw(self):
            """Called each frame to draw sprites and other assert on screen"""
            ...
    
    game = MyGame()
    batma.run()


------------
Requirements
------------

  - Python 2.6 or newer; Not tested in 3.x
  - Pyglet 1.1.4 or newer


----------
Installing
----------

Installing from source::

    python setup.py install


----
TODO
----

  - Sprite Collision
  - Maps

    - Camera
    - TileMap
    - IsometricMap
    - HexMap

  - Particles

    - ParticleEngine
    - Particles

  - Primitives (circle, squares, lines, points, etc... Backend to opengl) 
  - GUI
  - Genre specific modules (e.g. rpg, adventure, action, etc...)
  - Scaffolding system called "robi" lol 