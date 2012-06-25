========
Batma 2D
========

Batma is a pygame based game engine, inspired by XNA's structure. Providing an
intuitive framework for game development and other graphical applications.


--------
Features
--------

- Input state for keyboard and mouse;
- Sprites and Texts with easy rotation, scaling, positioning;
- 2D and 3D math library, including interpolation utilities;
- Scheduling of user defined functions;
- Scene based;


-------------
Game Workflow
-------------

Inspired by XNA, a Batma game follows almost the same structure::

    class MyGame(batma.Scene):
        def initialize(self):
            """Initializes game components, such screen properties"""
            ...
        
        def load_content(self):
            """Load game assets, such as sprites, fonts and sound effects"""
            ...

        def unload_content(self):
            '''Unload game assets'''
        
        def update(self, tick):
            """Called each frame, add all the game logic here"""
            ...
        
        def draw(self):
            """Called each frame to draw sprites and other assert on screen"""
            ...
    
    game = MyGame()
    batma.run(game)


------------
Requirements
------------

- Python 2.7+; Not tested in 3.x
- PyGame 1.9.1+;


----------
Installing
----------

Installing from source::

    python setup.py install
