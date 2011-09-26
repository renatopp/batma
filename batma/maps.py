# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

'''
Tile     - A standard sized bitmap image, part of a tile set, drawn as needed to 
           the display to make up a larger image/map
Tile Set - One or more Tile images combined into a single bitmap
Cell     - A portion of a tile-based map representing an area that is (for now) 
           the size of a single tile
Map      - A collection of Cells that forms a complete tile map
'''

from batma.sprite import Sprite

class Tile(object):
    def __init__(self, id, image):
        self.id = id
        self.image = image

class TileSet(object):
    def __init__(self, tiles):
        image = None
        self.tiles = tiles #dict
        self.tile_width = tiles.values()[0].width
        self.tile_height = tiles.values()[0].height

    def __getitem__(self, key):
        return self.tiles[key]
    
    def __setitem__(self, key, value):
        self.tiles[key] = value
    
    def get(self, key, default=None):
        return self.tiles.get(key, default)

class Cell(Sprite):
    def __init__(self, position, tile):
        super(Cell, self).__init__(tile, position, anchor=(0, 0))
        self.tile = tile

class TileMap(object):
    def __init__(self, width, height, tileset):
        self.width = width
        self.height = height
        self.tileset = tileset
        
        self.cells = []
        for x in xrange(width):
            col = []
            for y in xrange(height):
                p = x*tileset.tile_width, y*tileset.tile_height
                col.append(Cell(p, tileset[0]))
            self.cells.append(col)
        
        self.add_cell((0, 3), 3)
        self.add_cell((0, 4), 3)
        self.add_cell((0, 5), 1)
        self.add_cell((0, 6), 1)
        self.add_cell((0, 7), 1)
        self.add_cell((1, 3), 3)
        self.add_cell((1, 4), 1)
        self.add_cell((1, 5), 1)
        self.add_cell((1, 6), 1)
        self.add_cell((1, 7), 1)
        self.add_cell((2, 2), 3)
        self.add_cell((2, 3), 1)
        self.add_cell((2, 4), 1)
        self.add_cell((2, 5), 1)
        self.add_cell((2, 6), 1)
        self.add_cell((2, 7), 1)
        self.add_cell((3, 2), 3)
        self.add_cell((3, 3), 1)
        self.add_cell((3, 4), 1)
        self.add_cell((3, 5), 2)
        self.add_cell((3, 6), 2)
        self.add_cell((3, 7), 2)
        self.add_cell((4, 2), 3)
        self.add_cell((4, 3), 1)
        self.add_cell((4, 4), 1)
        self.add_cell((4, 5), 2)
        self.add_cell((4, 6), 2)
        self.add_cell((4, 7), 2)
        self.add_cell((5, 2), 3)
        self.add_cell((5, 3), 1)
        self.add_cell((5, 4), 1)
        self.add_cell((5, 5), 2)
        self.add_cell((5, 6), 2)
        self.add_cell((5, 7), 2)

    def add_cell(self, position, tile_id):
        p = position[0]*self.tileset.tile_width, position[1]*self.tileset.tile_height
        self[position] = Cell(p, self.tileset[tile_id])

    def __getitem__(self, key):
        return self.cells[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]] = value

    def get_rectangle(self):
        return self.cells

    def draw(self):
        rectangle = self.get_rectangle()
        tile_width = self.tileset.tile_width
        tile_height = self.tileset.tile_height
        for i in rectangle:
            for cell in i:
                cell.draw()
        
        

